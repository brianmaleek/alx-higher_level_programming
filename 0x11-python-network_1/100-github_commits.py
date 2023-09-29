#!/usr/bin/python3

"""
1. The Holberton School staff evaluates candidates applying for
    a back-end position with multiple technical challenges,
    like this one:
2. list 10 commits (from the most recent to oldest) of the
    repository “rails” by the user “rails”
3. You must use the GitHub API, here is the documentation
    https://developer.github.com/v3/repos/commits/
4. Print all commits by: `<sha>: <author name>` (one by line)
5. Python script that takes 2 arguments in order to solve this challenge.
        - First argument will be the repository name
        - Second argument will be the owner name
        - Must use the packages requests and sys
        - Only import requests and sys packages
        - No need to check arguments passed to the script (number or type)
"""


import requests
import sys

# Get the repository name and owner name from command line arguments
repo_name, owner_name = sys.argv[1], sys.argv[2]

# set url for the GitHub API
url = 'https://api.github.com/repos/{}/{}/commits'.\
    format(owner_name, repo_name)

try:
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
except Exception as e:
    print("An error occurred: {}".format(e))
