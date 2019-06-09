import os
import requests
from credentials import * 

# Setting user Parameters


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
        }

response = requests.post(baseUrl, json=data, headers=headers)
print(response.text)