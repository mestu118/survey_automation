import os
import requests
from credentials import * 

# Setting user Parameters
# apiToken = "mpqVbDZQGN9DBleFL0vm5X6g3AVmE3JLkULn7X3h" # Replace with Account API Token
# dataCenter = "nyu.ca1"

baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions".format(
    dataCenter)
headers = {
    "x-api-token": apiToken,
    "content-type": "application/json",
    "Accept": "application/json"
}

data = {"SurveyName": "My New Survey",
        "Language": "EN",
        "ProjectCategory": "CORE",
        "Published": True}

response = requests.post(baseUrl, json=data, headers=headers)
print(response.text)