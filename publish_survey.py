import os
import requests
from credentials import * 

surveyId = "SV_5jyf8FFOv7qK0Qt"


baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/versions".format(
    dataCenter, surveyId)

data = {
  "Description": "2018 New Survey Version",
  "Published": True
}

headers = {
   'accept': "application/json",
   'content-type': "application/json",
   "x-api-token": apiToken,
}

response = requests.post(baseUrl, json=data, headers=headers)

print(response.text)


# https://nyu.qualtrics.com/jfe/form/SV_5jyf8FFOv7qK0Qt

