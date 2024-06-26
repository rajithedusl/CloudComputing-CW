"""
This service would perform the calculation for the productivity metric for every developer and rank the developers
based on the score and would return the results to the client
test
"""
import json
import logging
from typing import List,Dict,Optional,Set
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import requests
import boto3
# import numpy as np
import ast
from boto3.dynamodb.conditions import Key
from DecimalEncoder import DecimalEncoder

app = FastAPI()

table_name = "seshat"
primary_key_column_name = "contributor_login"
columns = ["contribution_stats"]
# DB = boto3.resource('dynamodb')
# table = DB.Table(table_name)

@app.get("/")
def ping():
    return "PRODUCTIVITY CALCULATION SERVICE PING SUCCESSFUL : 200....THIS IS BLUE DEPLOYMENT"

# @app.get("/contributor-productivity")
# def get_contributor_productivity_calculation(repo:str,organization:str,contributor_login:str):
#     contributor_metrics_raw_response = table.get_item(
#         Key={
#             primary_key_column_name:contributor_login
#         }
#     )

#     if "Item" in contributor_metrics_raw_response: #CACHE HIT
#         print("CACHE HIT")
#         contributor_metrics_raw_response = contributor_metrics_raw_response["Item"]

#         print(contributor_metrics_raw_response)
#         contributor_metrics_raw_response = ast.literal_eval((json.dumps(contributor_metrics_raw_response,cls=DecimalEncoder)))
#         contributor_deviq_scores = {}
#         weekly_contributor_metrics = contributor_metrics_raw_response["contributor_stats"]["week"]
#         month_contributor_metrics  = contributor_metrics_raw_response["contributor_stats"]["month"]
#         yearly_contributor_metrics = contributor_metrics_raw_response["contributor_stats"]["year"]

#         time_frames  =  ["week","month","year"]
#         contrib_data_timeframe = [weekly_contributor_metrics,month_contributor_metrics,yearly_contributor_metrics]

#         for idx in range(len(contrib_data_timeframe)):
#             deviq_contributor_score = calculate_contributor_productivity(contrib_data_timeframe[idx])
#             time_frame = time_frames[idx]

#             contributor_deviq_scores[time_frame] = deviq_contributor_score


#         contributor_productivity_response  = {
#             "contributor_user_name" : contributor_login,
#             "contributor_productivity_scores": contributor_deviq_scores
#         }
#         return contributor_productivity_response
#     else:
#         print("CACHE MISS")
#         github_live_metrics = requests.request("GET",f"http://localhost:8001/contributor/snapshot?organization={organization}&repo={repo}&contributor={contributor_login}")

#         return github_live_metrics


# def calculate_contributor_productivity(raw_contributor_metrics:Dict):

#     total_deviq_score = None
#     try:
#         commit_additions = int(raw_contributor_metrics["commit_additions"])
#         commit_deletions = int(raw_contributor_metrics["commit_deletions"])
#         num_commits      = int(raw_contributor_metrics["num_commits"])
#         issues_created   = int(raw_contributor_metrics["issues_created"])
#         issues_comment_interactions = int(raw_contributor_metrics["issues_comment_interactions"])
#         print("NUM COMMITS : ",num_commits)
#         print("ISSUES CREATED : ",issues_created)
#         print("ISSUES_COMMENT_INTERACTIONS",issues_comment_interactions)
#         if commit_deletions and commit_deletions and num_commits != 0:
#             print('Hi')
#             # log_commit_contribution = round(np.log((commit_additions+commit_deletions)/num_commits),1)
#         else:
#             log_commit_contribution = 0
#         issue_contribution = issues_created+issues_comment_interactions
#         total_deviq_score = log_commit_contribution+issue_contribution

#     except KeyError as e:
#         print("EXCEPTION OCCURED: ",e)
#         print("RAW",raw_contributor_metrics)

#     return total_deviq_score


if __name__ == "__main__":
    uvicorn.run("productivity_calculation_service:app",host="0.0.0.0",port=8002,reload=True)
