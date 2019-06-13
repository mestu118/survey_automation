import os
import requests
from credentials import *
import sys
import json


def get_survey_def(apiToken, dataCenter, surveyId):
	# Setting user Parameters

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}".format(
	    dataCenter, surveyId)
	headers = {
	    "x-api-token": apiToken,
	}

	response = requests.get(baseUrl, headers=headers)
	text = json.loads(response.text)
	print(json.dumps(text, indent = 3))

def survey_creation(dataCenter, apiToken):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions"\
													.format(dataCenter)

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
	text = json.loads(response.text)
	print(json.dumps(text, indent = 3))
	return text['result']['SurveyID']

def activate_survey(dataCenter, apiToken):
	surveyId = "SV_5jyf8FFOv7qK0Qt"

	baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}".format(
	    dataCenter, surveyId)

	data = {
	  "isActive": False
	}

	headers = {
	   'accept': "application/json",
	   'content-type': "application/json",
	   "x-api-token": apiToken,
	}

	response = requests.put(baseUrl, json=data, headers=headers)

	print(response.text)


	# https://nyu.qualtrics.com/jfe/form/SV_5jyf8FFOv7qK0Qt

def publish_survey(dataCenter, surveyId, apiToken):
	surveyId = "SV_5jyf8FFOv7qK0Qt"
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/versions"\
														.format(dataCenter, surveyId)

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

def add_question(dataCenter, surveyId, apiToken):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions"\
	.format(dataCenter, surveyId)
	
	data = {
	"QuestionText": "AF200",
	"DefaultChoices": False,
    "DataExportTag": "Q3",
    "QuestionType": "DB",
    "Selector": "GRB",
    "SubSelector": "WOTXB",
    "Configuration": {
    	"QuestionDescriptionOption": "UseText"
	},
	"QuestionDescription": "AF200",
	"ChoiceOrder": [],
	"Validation": {
		"Settings": {
      	"Type": "None"
      	}
    },
	"GradingData": [],
	"Language": [],
	"NextChoiceId": 4,
	"NextAnswerId": 1,
	"Graphics": "IM_cwQH2NodZcgEORT",
	"GraphicsDescription": "AF200",
	"QuestionID": "QID3",
	"DataVisibility": {
   		"Private": False,
   		"Hidden": False
	},
	"QuestionText_Unsafe": "AF200"
	}

	headers = {
   'accept': "application/json",
   'content-type': "application/json",
   "x-api-token": apiToken,
	}

	response = requests.post(baseUrl, json=data, headers=headers)

	print(response.text)

def upload_image(dataCenter, apiToken):

	baseUrl = "https://{0}.qualtrics.com/API/v3//libraries/test/graphics"\
	.format(dataCenter)

	data =  "file=@Images/AF-203/CFD-AF-203-077-N.jpg;filename=Testing;type=image/jpeg"
	data = {'file': 'Images/AF-203/CFD-AF-203-077-N.jpg'}
	headers = {
   "x-api-token": apiToken,

	}

	response = requests.post(baseUrl, headers=headers, files=data)

	print(response.text)


if __name__ == '__main__':
	# surveyID = survey_creation(apiToken, apiToken)
	# add_question(dataCenter, 'SV_2aGKULkZOO41bb7', apiToken)
	upload_image(dataCenter, apiToken)






















