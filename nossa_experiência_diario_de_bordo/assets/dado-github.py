#!/usr/bin/env python3
"""
Script to collect comprehensive data from the GitHub organization "LabTechUDF"
for academic research in software management.

Features:
  - Fetches organization, member, repository, issue/PR, commit, timeline, and collaborator data.
  - Logs GitHub API rate limit details after live calls.
  - Caches every GET response in the "cache" folder to avoid repeated API calls.
  - Blacklists repositories (e.g., forks and specified repos) so they are skipped.
  - Retrieves extra member details for active organization members.
  - For relationship mapping, if a contributor (via commit/issue) is not an active member,
    fetches and saves their basic user data (id, node_id, login) with an extra flag "active": false.
  - Filters issues, commits, and timeline events to keep only required fields.
  - In relationship mapping, only contributors with non-zero contributions are saved.
  
Set your GitHub personal access token in the GITHUB_TOKEN environment variable.
"""

import os
import json
import time
import hashlib
import requests

# ------------------------------------------------------------------------------
# Global configuration
# ------------------------------------------------------------------------------
TOKEN = os.environ.get("GITHUB_TOKEN") or "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"
if not TOKEN:
    print("Please set the GITHUB_TOKEN environment variable with your GitHub personal access token.")
    exit(1)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# For timeline events (issues timeline API), we need a preview header.
TIMELINE_HEADERS = HEADERS.copy()
TIMELINE_HEADERS["Accept"] = "application/vnd.github.mockingbird-preview+json"

CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Define a list of repository names to blacklist.
REPO_BLACKLIST = [
    "Hi.Events",
    "demo-repository"
]

# ------------------------------------------------------------------------------
# Caching helpers
# ------------------------------------------------------------------------------

def get_cache_filename(url, params):
    """Generate a safe filename for caching based on the URL and parameters."""
    key_source = url
    if params:
        key_source += json.dumps(params, sort_keys=True)
    key = hashlib.md5(key_source.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{key}.json")

class CachedResponse:
    """A simple class to simulate a requests.Response object from cached data."""
    def __init__(self, json_data, headers, status_code=200):
        self._json = json_data
        self.headers = headers
        self.status_code = status_code

    def json(self):
        return self._json

# ------------------------------------------------------------------------------
# API GET function with caching and rate limit logging
# ------------------------------------------------------------------------------

def api_get(url, params=None, headers=HEADERS, force_update=False):
    """
    Perform a GET request with caching.
    If a cached file exists for the URL/params and force_update is False,
    returns a CachedResponse; otherwise, makes a live API call, logs rate-limit info,
    saves the response to cache, and returns the response.
    """
    cache_file = get_cache_filename(url, params)
    if not force_update and os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cached = json.load(f)
            print(f"[Cache] Using cached response for {url} with params={params}")
            return CachedResponse(cached["data"], cached.get("headers", {}), cached.get("status_code", 200))
        except Exception as e:
            print(f"[Cache] Error reading cache file {cache_file}: {e}")

    try:
        response = requests.get(url, params=params, headers=headers)
        if "X-RateLimit-Remaining" in response.headers:
            print(f"[Rate Limit] Limit: {response.headers.get('X-RateLimit-Limit')}, "
                  f"Used: {response.headers.get('X-RateLimit-Used')}, "
                  f"Remaining: {response.headers.get('X-RateLimit-Remaining')}, "
                  f"Reset: {response.headers.get('X-RateLimit-Reset')}")
        if response.status_code != 200:
            print(f"[Error] GET {url} returned {response.status_code}: {response.text}")
        try:
            cache_content = {
                "data": response.json(),
                "headers": dict(response.headers),
                "status_code": response.status_code
            }
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(cache_content, f, indent=2)
        except Exception as e:
            print(f"[Cache] Error writing cache file {cache_file}: {e}")
        return response
    except requests.RequestException as e:
        print(f"Request error for {url}: {e}")
        return None

def get_all_pages(url, params=None, headers=HEADERS):
    """
    Retrieve and aggregate all items from paginated endpoints.
    Follows the 'Link' header to fetch subsequent pages.
    """
    items = []
    while url:
        response = api_get(url, params=params, headers=headers)
        if response is None:
            break
        data = response.json()
        if isinstance(data, list):
            items.extend(data)
        else:
            items.append(data)
        link = response.headers.get("Link", None)
        if link:
            next_url = None
            parts = link.split(',')
            for part in parts:
                if 'rel="next"' in part:
                    next_url = part.split(';')[0].strip()[1:-1]
                    break
            url = next_url
            params = None
        else:
            break
    return items

def remove_template(url):
    """
    Remove trailing template tokens from a URL.
    Example: "https://api.github.com/orgs/LabTechUDF/members{/member}"
    becomes "https://api.github.com/orgs/LabTechUDF/members"
    """
    return url.split('{')[0]

# ------------------------------------------------------------------------------
# Filtering functions: Only keep needed fields.
# ------------------------------------------------------------------------------

def filter_user(user_obj):
    """Return a dictionary with only id, node_id, and login from a user object."""
    if not user_obj:
        return None
    return {
        "id": user_obj.get("id"),
        "node_id": user_obj.get("node_id"),
        "login": user_obj.get("login")
    }

def filter_issue(issue):
    """
    Filter an issue dictionary to only include the fields needed for analysis.
    For nested user objects, only keep id, node_id, and login.
    """
    filtered = {}
    keys_to_keep = [
        "url", "comments_url", "events_url", "id", "node_id", "number",
        "title", "state", "comments", "created_at", "updated_at", "closed_at",
        "sub_issues_summary", "body", "timeline_url"
    ]
    for key in keys_to_keep:
        filtered[key] = issue.get(key)
    filtered["user"] = filter_user(issue.get("user"))
    filtered["assignee"] = filter_user(issue.get("assignee"))
    filtered["assignees"] = [filter_user(a) for a in issue.get("assignees", [])]
    filtered["closed_by"] = filter_user(issue.get("closed_by"))
    pr = issue.get("pull_request")
    if pr:
        filtered["pull_request"] = {k: pr.get(k) for k in ["url", "html_url", "diff_url", "patch_url", "merged_at"]}
    else:
        filtered["pull_request"] = None
    return filtered

def filter_commit(commit_obj):
    """
    Filter a commit dictionary to only include the fields needed for analysis.
    For nested user objects, only keep id, node_id, and login.
    """
    filtered = {}
    keys_to_keep = ["sha", "node_id", "url", "comments_url"]
    for key in keys_to_keep:
        filtered[key] = commit_obj.get(key)
    filtered["commit"] = commit_obj.get("commit")  # This inner object is kept in full.
    filtered["commit"].pop("verification", None)  # Remove the 'verification' field.
    filtered["author"] = filter_user(commit_obj.get("author"))
    filtered["committer"] = filter_user(commit_obj.get("committer"))
    filtered["parents"] = commit_obj.get("parents")
    return filtered

def filter_timeline_event(event):
    """
    If a timeline event has an 'actor' or 'user' field, filter that field
    so it only contains id, node_id, and login.
    Returns a new event dictionary.
    """
    keys_to_remove = ["reactions", "verification"]
    filtered = event.copy()
    for key in keys_to_remove:
        filtered.pop(key, None)
    if "actor" in event:
        filtered["actor"] = filter_user(event["actor"])
    if "user" in event:
        filtered["user"] = filter_user(event["user"])
    if "review_requester" in event:
        filtered["review_requester"] = filter_user(event["review_requester"])
    if "requested_reviewer" in event:
        filtered["requested_reviewer"] = filter_user(event["requested_reviewer"])
    if "assignee" in event:
        filtered["assignee"] = filter_user(event["assignee"])
    return filtered

# ------------------------------------------------------------------------------
# Data fetching functions (unchanged)
# ------------------------------------------------------------------------------

def get_organization(org_name):
    url = f"https://api.github.com/orgs/{org_name}"
    response = api_get(url)
    if response:
        org_data = response.json()
        org_data["members_url"] = remove_template(org_data.get("members_url", ""))
        return {
            "url": org_data.get("url"),
            "repos_url": org_data.get("repos_url"),
            "issues_url": org_data.get("issues_url"),
            "members_url": org_data.get("members_url")
        }
    return None

def get_members(members_url):
    return get_all_pages(members_url)

def get_repositories(repos_url):
    return get_all_pages(repos_url)

def get_repo_issues(issues_url):
    url = remove_template(issues_url)
    return get_all_pages(url)

def get_repo_commits(commits_url):
    url = remove_template(commits_url)
    return get_all_pages(url)

def get_timeline_events(repo_full_name, issue_number):
    url = f"https://api.github.com/repos/{repo_full_name}/issues/{issue_number}/timeline"
    return get_all_pages(url, headers=TIMELINE_HEADERS)

def get_repo_collaborators(collaborators_url):
    url = remove_template(collaborators_url)
    return get_all_pages(url)


# ------------------------------------------------------------------------------
# Updated Relationship Mapping function
# ------------------------------------------------------------------------------
def build_relationship_mapping(repo, repo_issues, repo_commits, repo_collaborators, active_members, external_members):
    """
    Build a mapping (per contributor login) of:
      - Number of commits
      - Number of issues opened
      - Number of pull requests
    If a contributor is not among the active organization members,
    fetch and add their basic user data (if not already present) to external_members,
    tagging them as "active": False.
    Only include contributors with at least one contribution.
    """
    mapping = {}
    # Start with current collaborators.
    for collaborator in repo_collaborators:
        login = collaborator.get("login")
        if login:
            mapping[login] = {"commits": 0, "issues_opened": 0, "pull_requests": 0}

    # Process commits.
    for commit in repo_commits:
        author = commit.get("author")
        if author and "login" in author:
            login = author["login"]
            if login not in mapping:
                mapping[login] = {"commits": 0, "issues_opened": 0, "pull_requests": 0}
            mapping[login]["commits"] += 1

    # Process issues.
    for issue in repo_issues:
        user = issue.get("user")
        if user and "login" in user:
            login = user["login"]
            if login not in mapping:
                mapping[login] = {"commits": 0, "issues_opened": 0, "pull_requests": 0}
            mapping[login]["issues_opened"] += 1
            if "pull_request" in issue:
                mapping[login]["pull_requests"] += 1

    # Remove entries with zero total contributions.
    mapping = {login: stats for login, stats in mapping.items() if any(val > 0 for val in stats.values())}

    # For each contributor in mapping, if not active, add to external_members.
    for login in mapping:
        if login not in active_members:
            if login not in external_members:
                user_url = f"https://api.github.com/users/{login}"
                response = api_get(user_url)
                if response:
                    user_detail = filter_user(response.json())
                    user_detail["active"] = False
                    external_members[login] = user_detail
                else:
                    external_members[login] = {"id": None, "node_id": None, "login": login, "active": False}
    return mapping

def get_member_details(member):
    """
    For a given member dictionary (which must have the "url" field),
    fetch extra details and return a filtered user object.
    """
    user_url = member.get("url")
    response = api_get(user_url)
    if response:
        detail = response.json()
        return filter_user(detail)
    return filter_user(member)


# ------------------------------------------------------------------------------
# Main routine: data collection and saving
# ------------------------------------------------------------------------------
def main():
    org_name = "LabTechUDF"
    output = {}
    
    # 1. Organization Data
    print("Fetching organization data...")
    org_data = get_organization(org_name)
    if not org_data:
        print("Failed to fetch organization data.")
        return
    output["organization"] = org_data
    
    # 2. Members Data (active organization members; filtered)
    print("Fetching active members data...")
    members = get_members(org_data["members_url"])
    detailed_members = []
    for member in members:
        detailed = get_member_details(member)
        # Mark active members as active.
        detailed["active"] = True
        detailed_members.append(detailed)
    output["members"] = detailed_members
    # Build a lookup dictionary for active members.
    active_members = {member["login"]: member for member in detailed_members}
    # Prepare a dictionary to hold external (non-active) contributors.
    external_members = {}
    
    # 3. Repositories Data
    print("Fetching repositories data...")
    repos = get_repositories(org_data["repos_url"])
    repositories_list = []
    all_issues = {}
    all_commits = {}
    all_timeline_events = {}
    relationship_mapping = {}
    
    for repo in repos:
        repo_name = repo.get("name")
        if repo.get("fork") or repo_name in REPO_BLACKLIST:
            print(f"Skipping repository {repo_name} (fork or blacklisted)")
            continue

        print(f"Processing repository: {repo_name}")
        repo_info = {
            "name": repo_name,
            "html_url": repo.get("html_url"),
            "collaborators_url": remove_template(repo.get("collaborators_url", "")),
            "contributors_url": repo.get("contributors_url"),
            "commits_url": remove_template(repo.get("commits_url", "")),
            "teams_url": repo.get("teams_url"),
            "issue_events_url": repo.get("issue_events_url"),
            "subscribers_url": repo.get("subscribers_url"),
            "merges_url": repo.get("merges_url"),
            "issues_url": remove_template(repo.get("issues_url", "")),
            "pulls_url": remove_template(repo.get("pulls_url", "")),
            "language": repo.get("language"),
            "created_at": repo.get("created_at"),
            "updated_at": repo.get("updated_at"),
            "assignees_url": remove_template(repo.get("assignees_url", "")),
            "branches_url": remove_template(repo.get("branches_url", "")),
            "has_issues": repo.get("has_issues"),
            "has_projects": repo.get("has_projects"),
            "has_downloads": repo.get("has_downloads"),
            "forks": repo.get("forks"),
            "open_issues": repo.get("open_issues")
        }
        repositories_list.append(repo_info)
        repo_full_name = repo.get("full_name")
        
        # 4. Issues: fetch and filter.
        print(f"  Fetching issues for {repo_name}...")
        issues = get_repo_issues(repo.get("issues_url", ""))
        filtered_issues = [filter_issue(issue) for issue in issues]
        all_issues[repo_name] = filtered_issues
        
        # 5. Commits: fetch and filter.
        print(f"  Fetching commits for {repo_name}...")
        commits = get_repo_commits(repo.get("commits_url", ""))
        filtered_commits = [filter_commit(commit) for commit in commits]
        all_commits[repo_name] = filtered_commits
        
        # 6. Timeline events: fetch events for each issue and filter nested user data.
        timeline_events_repo = {}
        print(f"  Fetching timeline events for issues in {repo_name}...")
        for issue in issues:
            issue_number = issue.get("number")
            events = get_timeline_events(repo_full_name, issue_number)
            filtered_events = [filter_timeline_event(event) for event in events]
            timeline_events_repo[issue_number] = filtered_events
        all_timeline_events[repo_name] = timeline_events_repo
        
        # 7. Relationship Mapping: build mapping for contributors.
        print(f"  Building relationship mapping for {repo_name}...")
        collaborators = get_repo_collaborators(repo.get("collaborators_url", ""))
        mapping = build_relationship_mapping(repo, filtered_issues, filtered_commits, collaborators, active_members, external_members)
        relationship_mapping[repo_name] = mapping
        
        time.sleep(1)
    
    output["repositories"] = repositories_list
    output["issues"] = all_issues
    output["commits"] = all_commits
    output["timeline_events"] = all_timeline_events
    output["relationship_mapping"] = relationship_mapping
    
    # Merge external members into the overall members list.
    for login, member in external_members.items():
        if login not in active_members:
            output["members"].append(member)
    
    # 8. Save final collected data to a JSON file.
    output_filename = "labtechudf_data.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"Data collection complete. Saved to {output_filename}")

# ------------------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
