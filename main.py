from __future__ import print_function
from credentials import *
from write_spreadsheet import *
from read_spreadsheet import * 
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import requests
import sys
import json


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_survey_def(apiToken, dataCenter, surveyId):
	# Setting user Parameters

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}"\
												.format(dataCenter, surveyId)
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

	data = {
			"SurveyName": "My New Survey",
	        "Language": "EN",
	        "ProjectCategory": "CORE",
	        }

	response = requests.post(baseUrl, json=data, headers=headers)
	values = json.loads(response.text)
	print(values)
	return values['result']['DefaultBlockID'], values['result']['SurveyID']

def format_survey(apiToken, dataCenter, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/options"\
										.format(dataCenter, surveyId)

	data ={"BackButton": "false",
         "SaveAndContinue": "true",
         "SurveyProtection": "PublicSurvey",
         "BallotBoxStuffingPrevention": "false",
         "NoIndex": "Yes",
         "SecureResponseFiles": "true",
         "SurveyExpiration": None,
         "SurveyTermination": "DefaultMessage",
         "Header": "",
         "Footer": "",
         "ProgressBarDisplay": "None",
         "PartialData": "+1 week",
         "ValidationMessage": None,
         "PreviousButton": " \u2190 ",
         "NextButton": " \u2192 ",
         "SkinLibrary": "nyu",
         "SkinType": "templated",
         "Skin": {
            "brandingId": None,
            "templateId": "*2014",
            "overrides": {
               "font": {
                  "family": "arial, helvetica, sans-serif"
               },
               "contrast": 0
            }
         },
         "NewScoring": 1,
         "CustomStyles": [],
         "EOSMessage": "",
         "ShowExportTags": "false",
         "CollectGeoLocation": "false",
         "SurveyTitle": "Online Survey Software | Qualtrics Survey Solutions",
         "SurveyMetaDescription": "Qualtrics sophisticated online survey software solutions make creating online surveys easy. Learn more about Research Suite and get a free account today.",
         "PasswordProtection": "No",
         "AnonymizeResponse": "No",
         "Password": "",
         "RefererCheck": "No",
         "RefererURL": "http://",
         "UseCustomSurveyLinkCompletedMessage": None,
         "SurveyLinkCompletedMessage": "",
         "SurveyLinkCompletedMessageLibrary": "",
         "ResponseSummary": "No",
         "EOSMessageLibrary": "",
         "EOSRedirectURL": "https://",
         "EmailThankYou": "false",
         "ThankYouEmailMessageLibrary": None,
         "ThankYouEmailMessage": None,
         "ValidateMessage": "false",
         "ValidationMessageLibrary": None,
         "InactiveSurvey": "DefaultMessage",
         "PartialDataCloseAfter": "LastActivity",
         "ActiveResponseSet": "RS_2f0DHB6QFMErpY1",
         "InactiveMessageLibrary": "",
         "InactiveMessage": "",
         "AvailableLanguages": {
            "EN": []
         },
         "SurveyLanguage": "EN",
         "SurveyStartDate": None,
         "SurveyExpirationDate": None,
         "SurveyCreationDate": "2019-07-09T17:48:00Z"
		}

	headers = {
	   'accept': "application/json",
	   'content-type': "application/json",
	   "x-api-token": apiToken,
	}

	response = requests.put(baseUrl, json=data, headers=headers)

	print(response.text)

def activate_survey(apiToken, dataCenter, surveyId):
	baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}"\
								.format(dataCenter, surveyId)

	data = {
	  "isActive": True
	}

	headers = {
	   'accept': "application/json",
	   'content-type': "application/json",
	   "x-api-token": apiToken,
	}

	response = requests.put(baseUrl, json=data, headers=headers)
	values = json.loads(response.text)

	print(values)

def add_image(apiToken, dataCenter, surveyId, image_id):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions"\
	.format(dataCenter, surveyId)
	
	data = {
            "QuestionText": "<span style=\"font-size: 12pt; font-family: Calibri, Arial; color: rgb(0, 0, 0);\" data-sheets-value=\"{&quot;1&quot;:2,&quot;2&quot;:&quot;You are hiring an Apple specialist for a temporary position.\\nWhat hourly wage will you offer the following candidate?&quot;}\" data-sheets-userformat=\"{&quot;2&quot;:14593,&quot;3&quot;:{&quot;1&quot;:0,&quot;3&quot;:1},&quot;11&quot;:4,&quot;14&quot;:[null,2,0],&quot;15&quot;:&quot;Calibri&quot;,&quot;16&quot;:12}\">You are hiring an Apple specialist for a temporary position.<br>What hourly wage will you offer the following candidate?</span>",
            "DefaultChoices": False,
            "DataExportTag": "Q1",
            "QuestionID": "QID1",
            "QuestionType": "DB",
            "Selector": "GRB",
            "SubSelector": "WTXB",
            "Configuration": {
               "QuestionDescriptionOption": "UseText"
            },
            "QuestionDescription": "You are hiring an Apple specialist for a temporary position. What hourly wage will you offer the...",
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
            "Graphics": image_id,
            "GraphicsDescription": "AF-201",
            "QuestionText_Unsafe": "<span style=\"font-size: 12pt; font-family: Calibri, Arial; color: rgb(0, 0, 0);\" data-sheets-value=\"{&quot;1&quot;:2,&quot;2&quot;:&quot;You are hiring an Apple specialist for a temporary position.\\nWhat hourly wage will you offer the following candidate?&quot;}\" data-sheets-userformat=\"{&quot;2&quot;:14593,&quot;3&quot;:{&quot;1&quot;:0,&quot;3&quot;:1},&quot;11&quot;:4,&quot;14&quot;:[null,2,0],&quot;15&quot;:&quot;Calibri&quot;,&quot;16&quot;:12}\">You are hiring an Apple specialist for a temporary position.<br>What hourly wage will you offer the following candidate?</span>"
         }

	headers = {
   'accept': "application/json",
   'content-type': "application/json",
   "x-api-token": apiToken,
	}

	response = requests.post(baseUrl, json=data, headers=headers)
	values = json.loads(response.text)
	print(response.text)
	return values['result']['QuestionID']

def add_question(apiToken, dataCenter, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions"\
	.format(dataCenter, surveyId)
	
	data = {
		"QuestionText": "Hourly Wage:",
            "DataExportTag": "Q2",
            "QuestionType": "MC",
            "Selector": "SAHR",
            "SubSelector": "TX",
            "Configuration": {
               "QuestionDescriptionOption": "UseText",
               "LabelPosition": "BELOW"
            },
            "QuestionDescription": "Hourly Wage:",
            "Choices": {
               "1": {
                  "Display": "$15"
               },
               "2": {
                  "Display": "$16"
               },
               "3": {
                  "Display": "$17"
               },
               "4": {
                  "Display": "$18"
               },
               "5": {
                  "Display": "$19"
               },
               "6": {
                  "Display": "$20"
               },
               "7": {
                  "Display": "$21"
               },
               "8": {
                  "Display": "$22"
               },
               "9": {
                  "Display": "$23"
               },
               "10": {
                  "Display": "$24"
               },
               "11": {
                  "Display": "$25"
               }
            },
            "ChoiceOrder": [
               1,
               2,
               3,
               4,
               5,
               6,
               7,
               8,
               9,
               10,
               11
            ],
            "Validation": {
               "Settings": {
                  "ForceResponse": "OFF",
                  "ForceResponseType": "ON",
                  "Type": "None"
               }
            },
            "Language": [],
            "NextChoiceId": 12,
            "NextAnswerId": 1,
            "QuestionID": "QID2",
            "QuestionText_Unsafe": "Hourly Wage:"
         }

	headers = {
   'accept': "application/json",
   'content-type': "application/json",
   "x-api-token": apiToken,
	}

	response = requests.post(baseUrl, json=data, headers=headers)
	values = json.loads(response.text)
	return values['result']['QuestionID']

def publish_survey(dataCenter, apiToken, surveyId):
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

	values = json.loads(response.text)
	print(values)
	return values['result']['metadata']['surveyID']


def delete_images(dataCenter, apiToken, image_id):
	baseUrl = "https://{0}.qualtrics.com/API/v3/libraries/UR_2oCfkV4WwzhNcih/graphics/{1}".format(dataCenter, image_id)
	headers = {
	"x-api-token":apiToken
	}
	response = requests.delete(baseUrl, headers = headers)
	print(response)

def upload_image(dataCenter, apiToken, image_dir, description):

	baseUrl = "https://{0}.qualtrics.com/API/v3/libraries/UR_2oCfkV4WwzhNcih/graphics".format(dataCenter)
	file = {'file': (description, open(image_dir,'rb'), 'image/jpeg')}
	headers = {
	"x-api-token": apiToken
	}

	response = requests.post(baseUrl, headers=headers, files=file)
	print(response.text)
	values = json.loads(response.text)
	return values['result']['id']

def upload_all_images(dataCenter, apiToken, service):
	data = [['Image Folder', 'Image ID']]
	for f in os.listdir('Images'):
		images = os.listdir('Images/' + f)
		image_dir = 'Images/' + f + '/' + str(images[0])
		image_id = upload_image(dataCenter, apiToken, image_dir, f)
		data.append([f, image_id])
	write_to_spreadsheet(data, service)

def create_block(dataCenter, apiToken, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/blocks"\
														.format(dataCenter, surveyId)
	data = {"Type": "Standard",
	"Description": "My Block Name",
	"Options": {
	"BlockLocking": "false",
	"RandomizeQuestions": "false",
	"BlockVisibility": "Collapsed"}
	}

	headers = {
	   'accept': "application/json",
	   'content-type': "application/json",
	   "x-api-token": apiToken,
	}

	response = requests.post(baseUrl, json = data, headers = headers)
	values = json.loads(response.text)
	return values['result']['BlockID'], values['result']['FlowID']

def update_block(dataCenter, apiToken, surveyId, blockId, questionIds):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/blocks/{2}"\
														.format(dataCenter, surveyId, blockId)
	questions = []
	for question in questionIds:
		questions.append(
			{"Type": "Question",
			"QuestionID" : question})
	data = {"Type": "Standard",
			"Description": "My Block Name",
			"BlockElements": questions,
			"Options": {
			"BlockLocking": "false",
			"RandomizeQuestions": "false",
			"BlockVisibility": "Collapsed"
			}
			}

	headers = {
	   'accept': "application/json",
	   'content-type': "application/json",
	   "x-api-token": apiToken,
	}

	response = requests.put(baseUrl, json = data, headers = headers)

def delete_block(dataCenter, apiToken, surveyId, blockId):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/blocks/{2}"\
										.format(dataCenter, surveyId, blockId)
	
	headers = {
	   "x-api-token": apiToken
	}

	response = requests.delete(baseUrl, headers = headers)
	print(response.text)


def update_flow(dataCenter, apiToken, surveyId, flows, blocks, defaultId):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/flow".format(dataCenter, surveyId)
	temp = []
	for flow, block in zip(flows, blocks):
		temp.append({
			"ID" : block,
			"Type" : "Block",
			"FlowID" : flow
			})

	data = {"Flow" : temp,
	"FlowID": "FL_1",
    "Properties": {
        "Count": 2,
        "RemovedFieldsets": []
    },
    "Type": "Root"}

	headers = {
	   'accept': "application/json",
	   'content-type': "application/json",
	   "x-api-token": apiToken,
	}

	response = requests.put(baseUrl, json = data, headers = headers)
	values = json.loads(response.text)
	print(values)

if __name__ == '__main__':
	"""Shows basic usage of the Sheets API.
	Prints values from a sample spreadsheet.
	"""
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials_web.json', SCOPES)
			creds = flow.run_local_server()
			# Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)


	service = build('sheets', 'v4', credentials=creds)
	#Only needed when need to upload all of the images onto Qualtrics
	#upload_all_images(dataCenter, apiToken, service)

	images, questions = read_item_spreadsheet(service)
	imageToId = read_image_spreadsheet(service)
	##Create survey
	defaultBlock, surveyId = survey_creation(dataCenter, apiToken)
	format_survey(apiToken, dataCenter, surveyId)

	counter = 0 
	flows = []
	blocks = []
	for i in range(len(images)):
		value = images[i]
		question = questions[i][0]
		folder = value[0]
		questionIDs = [] 
		if folder in imageToId:
			print("creating block")
			blockID, flowID = create_block(dataCenter, apiToken, surveyId)
			flows.append(flowID)
			blocks.append(blockID)
			print("adding image")
			ID = add_image(apiToken, dataCenter, surveyId, imageToId[folder])
			questionIDs.append(ID)
			print("adding question")
			ID = add_question(apiToken, dataCenter, surveyId)
			questionIDs.append(ID)
			print("updating block")
			update_block(dataCenter, apiToken, surveyId, blockID, questionIDs)
			counter += 1
		if counter == 3:
			break

	update_flow(dataCenter, apiToken, surveyId, flows, blocks, defaultBlock)
	publish_survey(dataCenter, apiToken, surveyId)
	activate_survey(apiToken, dataCenter, surveyId)
	print("https://nyu.qualtrics.com/jfe/form/{}".format(surveyId))
	# print(surveyId)
	# get_survey_def(apiToken, dataCenter, surveyId)
























