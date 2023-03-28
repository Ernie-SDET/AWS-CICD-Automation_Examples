#!/usr/bin/env python3
"""
Lambda handler 'LogTriggeredCodeCommitInfo.py'
will be triggered by CodeCommit events and perform the tollowing tasks:

1. Exract CodeCommit references
2. Extract the most recent commitID
3. Extract detail about the commit ('who', 'what' 'when' etc.)
4. Extract dictionaries ordered alphabetically by FileName(s) found in the repo
5. Transform Gregorian date info associated with AUTHOR and COMMITTER
6. Store results of these asctions in a CLoudWatch Log stream.

EXECUTION ROLE requires the following permissions:
    AWSCodeCommitReadOnly
    AWSLambda_FullAccess
    CloudWatchLogsFullAccess
"""
from datetime import datetime
import boto3
import json
import logging

codecommit = boto3.client('codecommit')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    # Extract repository name from the event.
    repo_name = event['Records'][0]['eventSourceARN'].split(':')[5]
    time_now = datetime.now()
    logger.info(f"Codecommit repository '{repo_name}' update trigger event processing STARTED:{time_now}")

    #Extract dictionary data, from a list, into dictionary 'commit_info'.
    commit_info = {}
    commit_info = event['Records'][0]['codecommit']['references']
    logger.debug(f"Repository '{repo_name}' general_commit_info == {commit_info}")

    # Extract git_references data from the dictionary.
    git_references = [ key['ref'] for key in commit_info ]
    logger.info(f"Repository '{repo_name}' git_references == {git_references}")

    # Extract commit_references list from the dictionary.
    # Convert list to string via x.strip("], ', ["")
    commit_references = [ key['commit'] for key in commit_info ]
    temp = str(commit_references)
    commit_str = temp.strip("], ', [")
    logger.info(f"Most recent repository CommitID: '{commit_references}'")

    # Temporarily uncomment the following line to make the repository name invalid.
    ### repo_name += '-InvalidName'
    # Display repository's git clone URL
    try:
        event_response = codecommit.get_repository(repositoryName=repo_name)
        # Extract detail about the commit
        commit_detail = codecommit.get_commit(repositoryName=repo_name, commitId=commit_str)
        logger.info(f"commit detail == {commit_detail}")
        commit_response = (codecommit.get_differences(repositoryName=repo_name,
            afterCommitSpecifier=event['Records'][0]['codecommit']['references'][0]['commit']))
        count = len(commit_response['differences'])
        logger.debug(f"commit_response[differences] dictionary count == '{count}'")
        logger.debug(f"commit_response == '{commit_response}'")

        # Extract 'who' and 'when' commit detail
        who_author = commit_detail['commit']['author']['name']
        who_committer = commit_detail['commit']['committer']['name']
        when_author = commit_detail['commit']['author']['date']
        when_committer = commit_detail['commit']['committer']['date']

        idx = 0
        timestamp = ' '
        # Remove timezone data
        while idx < (len(when_author) - 6):
            timestamp += when_author[idx]
            idx +=1
        logger.debug(f"timestamp == '{timestamp}'")
        dt_obj = datetime.fromtimestamp(int(timestamp))
        logger.info(f"AUTHOR {who_author}'s Gregorian date tranformation == {dt_obj}")

        idx = 0
        timestamp = ' '
        # Remove timezone data
        while idx < (len(when_committer) - 6):
            timestamp += when_committer[idx]
            idx +=1
        logger.debug(f"timestamp == '{timestamp}'")
        dt_obj = datetime.fromtimestamp(int(timestamp))
        logger.info(f"COMMITTER {who_committer}'s Gregorian date transformation == {dt_obj}")

        ### count = 0
        # Extract dictionaries ordered alphabetically by FileName(s) found in the repo
        for idx in range(0, count):
            logger.info(f"{idx+ 1} of {count} - {commit_response['differences'][idx]}")
        logger.info(f"Codecommit repository '{repo_name}' update trigger event processing COMPLETED:{time_now}")
        logger.info(f"Clone URL: {event_response['repositoryMetadata']['cloneUrlHttp']}")
        results = event_response['repositoryMetadata']['cloneUrlHttp']
        return
    except Exception as e:
        logger.error(f"Error getting repository '{repo_name}'. Make sure it exists and that your repository is in the same region as this function.")
        raise e
    return
# EOF
