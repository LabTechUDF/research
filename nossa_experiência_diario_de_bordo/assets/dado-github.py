#!/usr/bin/env python3
"""
Script to collect comprehensive data from the GitHub organization "LabTechUDF"
for academic research in software management.

Features:
  - Fetches organization, member, repository, issue/PR, commit, timeline,
    and collaborator data.
  - Logs GitHub API rate limit details after live calls.
  - Caches every GET response to a file in the "cache" folder so that
    subsequent runs can use stored data (avoiding extra API calls).

Set your GitHub personal access token in the environment variable GITHUB_TOKEN.
"""

import os
import json
import time
import hashlib
import requests

# ------------------------------------------------------------------------------
# Global configuration
# ------------------------------------------------------------------------------
TOKEN = os.environ.get("GITHUB_TOKEN")
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

# ------------------------------------------------------------------------------
# Caching helpers
# ------------------------------------------------------------------------------

def get_cache_filename(url, params):
    """
    Generate a safe filename for caching based on the URL and parameters.
    """
    key_source = url
    if params:
        # Sort parameters to get a consistent key.
        key_source += json.dumps(params, sort_keys=True)
    key = hashlib.md5(key_source.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{key}.json")

class CachedResponse:
    """
    A simple class to simulate a requests.Response object from cached data.
    """
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
    Perform a GET request to the specified URL with caching.
    If a cached file exists for the same URL/params and force_update is False,
    returns a CachedResponse. Otherwise, makes a live API call, logs rate limit
    info, saves the response to cache, and returns the response.
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
        # Log rate limit details if available.
        if "X-RateLimit-Remaining" in response.headers:
            print(f"[Rate Limit] Limit: {response.headers.get('X-RateLimit-Limit')}, "
                  f"Used: {response.headers.get('X-RateLimit-Used')}, "
                  f"Remaining: {response.headers.get('X-RateLimit-Remaining')}, "
                  f"Reset: {response.headers.get('X-RateLimit-Reset')}")
        if response.status_code != 200:
            print(f"[Error] GET {url} returned {response.status_code}: {response.text}")
            # Optionally, you could cache errors as well to avoid repeated calls.
        # Cache the response
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
    Follows the 'Link' header to get next pages.
    Uses the caching-enabled api_get function.
    Returns a list of items.
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
        # Check for pagination using the Link header.
        link = response.headers.get("Link", None)
        if link:
            next_url = None
            parts = link.split(',')
            for part in parts:
                if 'rel="next"' in part:
                    next_url = part.split(';')[0].strip()[1:-1]
                    break
            url = next_url
            params = None  # subsequent pages already include query parameters in the URL.
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
# Data fetching functions
# ------------------------------------------------------------------------------

def get_organization(org_name):
    """
    Fetch organization information and remove template tokens.
    Returns a dictionary with selected fields.
    """
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

def build_relationship_mapping(repo, repo_issues, repo_commits, repo_collaborators):
    """
    Build a mapping (per collaborator login) of:
      - Number of commits
      - Number of issues opened
      - Number of pull requests
    """
    mapping = {}
    for collaborator in repo_collaborators:
        login = collaborator.get("login")
        mapping[login] = {"commits": 0, "issues_opened": 0, "pull_requests": 0}
    for commit in repo_commits:
        author = commit.get("author")
        if author and "login" in author:
            login = author["login"]
            if login in mapping:
                mapping[login]["commits"] += 1
    for issue in repo_issues:
        user = issue.get("user")
        if user and "login" in user:
            login = user["login"]
            if login in mapping:
                mapping[login]["issues_opened"] += 1
            if "pull_request" in issue and login in mapping:
                mapping[login]["pull_requests"] += 1
    return mapping

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
    
    # 2. Members Data
    print("Fetching members data...")
    members = get_members(org_data["members_url"])
    output["members"] = [{
        "login": member.get("login"),
        "id": member.get("id"),
        "html_url": member.get("html_url")
    } for member in members]
    
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
        repo_full_name = repo.get("full_name")  # e.g., "LabTechUDF/python-services"
        
        # 4. Issues
        print(f"  Fetching issues for {repo_name}...")
        issues = get_repo_issues(repo.get("issues_url", ""))
        all_issues[repo_name] = issues
        
        # 5. Commits
        print(f"  Fetching commits for {repo_name}...")
        commits = get_repo_commits(repo.get("commits_url", ""))
        all_commits[repo_name] = commits
        
        # 6. Timeline events (for each issue)
        timeline_events_repo = {}
        print(f"  Fetching timeline events for issues in {repo_name}...")
        for issue in issues:
            issue_number = issue.get("number")
            events = get_timeline_events(repo_full_name, issue_number)
            timeline_events_repo[issue_number] = events
        all_timeline_events[repo_name] = timeline_events_repo
        
        # 7. Relationship Mapping: collaborators vs. contributions.
        print(f"  Fetching collaborators for {repo_name}...")
        collaborators = get_repo_collaborators(repo.get("collaborators_url", ""))
        mapping = build_relationship_mapping(repo, issues, commits, collaborators)
        relationship_mapping[repo_name] = mapping
    
    output["repositories"] = repositories_list
    output["issues"] = all_issues
    output["commits"] = all_commits
    output["timeline_events"] = all_timeline_events
    output["relationship_mapping"] = relationship_mapping
    
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
