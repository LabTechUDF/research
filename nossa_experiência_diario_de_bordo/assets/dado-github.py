#!/usr/bin/env python3
"""
Script to collect comprehensive data from the GitHub organization "LabTechUDF"
for academic research in software management. Data collected includes:
  - Organization information
  - Organization members
  - Repositories and selected repository fields
  - Issues and (if available) pull request data per repository
  - Commits (with commit messages, author/committer details)
  - Timeline events for issues (e.g. creation/closing events)
  - Relationship mapping: for each repo, compare collaborators with users
    who have contributed (via commits, issues, or pull requests)

The output is saved to a structured JSON file ("labtechudf_data.json").
This dataset will later be used to generate graphs such as pie charts,
histograms, line charts, stacked bar charts, and network graphs.
"""

import os
import json
import time
import requests

# ------------------------------------------------------------------------------
# Global configuration
# ------------------------------------------------------------------------------
# Get your personal access token from the environment variable GITHUB_TOKEN.
TOKEN = os.environ.get("GITHUB_TOKEN") | "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"
if not TOKEN:
    print("Please set the GITHUB_TOKEN environment variable with your GitHub personal access token.")
    exit(1)

# Basic headers for GitHub API requests.
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# For timeline events the GitHub API requires a special preview Accept header.
TIMELINE_HEADERS = HEADERS.copy()
TIMELINE_HEADERS["Accept"] = "application/vnd.github.mockingbird-preview+json"

# ------------------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------------------

def api_get(url, params=None, headers=HEADERS):
    """
    Perform a GET request to the specified URL with error handling.
    Returns the Response object if successful, otherwise None.
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching {url}: {response.status_code} {response.text}")
            return None
        return response
    except requests.RequestException as e:
        print(f"Request error for {url}: {e}")
        return None

def get_all_pages(url, params=None, headers=HEADERS):
    """
    Retrieve and aggregate all items from paginated endpoints.
    Uses the 'Link' header to follow 'next' pages.
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
        # Check for pagination via the Link header.
        link = response.headers.get("Link", None)
        if link:
            next_url = None
            # The Link header has the format: <url>; rel="next", <url>; rel="last", etc.
            parts = link.split(',')
            for part in parts:
                if 'rel="next"' in part:
                    next_url = part.split(';')[0].strip()[1:-1]
                    break
            url = next_url
            params = None  # after first page, params are embedded in URL
        else:
            break
    return items

def remove_template(url):
    """
    Remove trailing template tokens from GitHub API URLs.
    For example, converts:
      "https://api.github.com/orgs/LabTechUDF/members{/member}"
    into:
      "https://api.github.com/orgs/LabTechUDF/members"
    """
    return url.split('{')[0]

# ------------------------------------------------------------------------------
# Data fetching functions
# ------------------------------------------------------------------------------

def get_organization(org_name):
    """
    Fetch basic organization information and remove tokens from URLs.
    Returns a dictionary with selected fields.
    """
    url = f"https://api.github.com/orgs/{org_name}"
    response = api_get(url)
    if response:
        org_data = response.json()
        # Remove trailing template tokens from members_url.
        org_data["members_url"] = remove_template(org_data.get("members_url", ""))
        return {
            "url": org_data.get("url"),
            "repos_url": org_data.get("repos_url"),
            "issues_url": org_data.get("issues_url"),
            "members_url": org_data.get("members_url")
        }
    return None

def get_members(members_url):
    """
    Retrieve all organization members.
    """
    return get_all_pages(members_url)

def get_repositories(repos_url):
    """
    Retrieve all repositories in the organization.
    """
    return get_all_pages(repos_url)

def get_repo_issues(issues_url):
    """
    Retrieve all issues for a repository.
    Removes any trailing URL tokens.
    """
    url = remove_template(issues_url)
    return get_all_pages(url)

def get_repo_commits(commits_url):
    """
    Retrieve all commits for a repository.
    Removes any trailing URL tokens.
    """
    url = remove_template(commits_url)
    return get_all_pages(url)

def get_timeline_events(repo_full_name, issue_number):
    """
    Retrieve timeline events for a given issue using the timeline API.
    Requires the preview Accept header.
    """
    url = f"https://api.github.com/repos/{repo_full_name}/issues/{issue_number}/timeline"
    return get_all_pages(url, headers=TIMELINE_HEADERS)

def get_repo_collaborators(collaborators_url):
    """
    Retrieve the list of collaborators for a repository.
    Removes trailing tokens from the URL.
    """
    url = remove_template(collaborators_url)
    return get_all_pages(url)

def build_relationship_mapping(repo, repo_issues, repo_commits, repo_collaborators):
    """
    For a given repository, build a mapping of collaborator contributions.
    For each collaborator (by login), count how many commits, issues, and pull requests they made.
    """
    mapping = {}
    # Initialize mapping for each collaborator.
    for collaborator in repo_collaborators:
        login = collaborator.get("login")
        mapping[login] = {
            "commits": 0,
            "issues_opened": 0,
            "pull_requests": 0
        }
    # Count commits: use commit['author'] if available.
    for commit in repo_commits:
        author = commit.get("author")
        if author and "login" in author:
            login = author["login"]
            if login in mapping:
                mapping[login]["commits"] += 1
    # Count issues and pull requests:
    for issue in repo_issues:
        user = issue.get("user")
        if user and "login" in user:
            login = user["login"]
            if login in mapping:
                mapping[login]["issues_opened"] += 1
            # If the issue has a "pull_request" key, count it as a pull request.
            if "pull_request" in issue and login in mapping:
                mapping[login]["pull_requests"] += 1
    return mapping

# ------------------------------------------------------------------------------
# Main data collection routine
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
    members_list = []
    for member in members:
        members_list.append({
            "login": member.get("login"),
            "id": member.get("id"),
            "html_url": member.get("html_url")
        })
    output["members"] = members_list
    
    # 3. Repositories Data
    print("Fetching repositories data...")
    repos = get_repositories(org_data["repos_url"])
    repositories_list = []
    all_issues = {}          # Key: repo name, value: list of issues
    all_commits = {}         # Key: repo name, value: list of commits
    all_timeline_events = {} # Key: repo name, value: dict mapping issue number -> timeline events
    relationship_mapping = {}# Key: repo name, value: relationship mapping dictionary
    
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
        
        # 4. Issues and Pull Requests Data for the repository.
        print(f"  Fetching issues for {repo_name}...")
        issues = get_repo_issues(repo.get("issues_url", ""))
        all_issues[repo_name] = issues
        
        # 5. Commits Data
        print(f"  Fetching commits for {repo_name}...")
        commits = get_repo_commits(repo.get("commits_url", ""))
        all_commits[repo_name] = commits
        
        # 5. Timeline Events (for each issue)
        timeline_events_repo = {}
        print(f"  Fetching timeline events for issues in {repo_name}...")
        for issue in issues:
            issue_number = issue.get("number")
            events = get_timeline_events(repo_full_name, issue_number)
            timeline_events_repo[issue_number] = events
        all_timeline_events[repo_name] = timeline_events_repo
        
        # 6. Relationship Mapping: collaborators vs. contributions
        print(f"  Fetching collaborators for {repo_name}...")
        collaborators = get_repo_collaborators(repo.get("collaborators_url", ""))
        mapping = build_relationship_mapping(repo, issues, commits, collaborators)
        relationship_mapping[repo_name] = mapping
        
        # Small delay to help avoid hitting rate limits
        time.sleep(1)
    
    output["repositories"] = repositories_list
    output["issues"] = all_issues
    output["commits"] = all_commits
    output["timeline_events"] = all_timeline_events
    output["relationship_mapping"] = relationship_mapping
    
    # 8. Save collected data to a JSON file.
    output_filename = "labtechudf_data.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"Data collection complete. Saved to {output_filename}")

# ------------------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
