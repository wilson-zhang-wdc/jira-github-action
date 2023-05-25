from jira import JIRA
import sys
import os
import re

# Jira server information
JIRA_SERVER = 'https://cejira.sandisk.com'

# Update the status of a Jira issue
def update_jira_issue_status(username, password, issue_key, status):
    # Connect to Jira
    jira = JIRA(server=JIRA_SERVER, basic_auth=(username, password))

    # Get the issue
    issue = jira.issue(issue_key)
    print(issue)

    # # Transition the issue to the desired status
    # transitions = jira.transitions(issue)
    # transition_id = None
    # for transition in transitions:
    #     if transition['to']['name'].lower() == status.lower():
    #         transition_id = transition['id']
    #         break

    # if transition_id:
    #     jira.transition_issue(issue, transition_id)
    #     print(f'Updated Jira issue status to: {status}')
    # else:
    #     print(f'Could not find transition to status: {status}')

# Example usage
if __name__ == '__main__':
    # Retrieve username and password from command-line arguments or environment variables
    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]    
        commit_message = sys.argv[3]
    else:
        print(rf"Expected 3 parameters, only {len(sys.argv)-1} were provided")
        sys.exit(1)

    jira_key = re.search("STAR-[0-9]+", commit_message)
    print(jira_key)

    # update_jira_issue_status(username, password, jira_key, 'In Progress')