from jira import JIRA
import sys
import os
import re
import json

# Retrieve username and password from command-line arguments or environment variables
if len(sys.argv) >= 4:
    username = sys.argv[1]
    password = sys.argv[2]    
    github_data = json.loads(sys.argv[3])
else:
    print(rf"Expected 3 parameters, only {len(sys.argv)-1} were provided")
    sys.exit(1)

commit_message = github_data["event"]["head_commit"]["message"]

# Extract jira key from commit message
jira_key = re.search("STAR-[0-9]+", commit_message).group()
print(jira_key)

# Jira server information
JIRA_SERVER = 'https://cejira.sandisk.com'

# Connect to Jira
jira = JIRA(server=JIRA_SERVER, basic_auth=(username, password))

# Get the issue
issue = jira.issue(jira_key)
print(issue)