import os
import requests
import sys
import json
from credentials import *
from write_spreadsheet import * 

#Note: apiToken & dataCenter imported from credentials 

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
	print(response.text)

def update_survey(apiToken, dataCenter, surveyId):

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
	surveyId = "SV_5jyf8FFOv7qK0Qt"

	baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}"\
								.format(dataCenter, surveyId)

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

def add_image(apiToken, dataCenter, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions"\
	.format(dataCenter, surveyId)
	
	data = {
            "QuestionText": "Test",
            "DefaultChoices": False,
            "DataExportTag": "Q1",
            "QuestionType": "DB",
            "Selector": "GRB",
            "SubSelector": "WOTXB",
            "Configuration": {
               "QuestionDescriptionOption": "UseText"
            },
            "QuestionDescription": "Test",
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
            "Graphics": "IM_9ugk7ACap1CH7zn",
            "GraphicsDescription": "Cfd af 201 060 n",
            "QuestionID": "QID1",
            "QuestionText_Unsafe": "Cfd af 201 060 n"
         }

	headers = {
   'accept': "application/json",
   'content-type': "application/json",
   "x-api-token": apiToken,
	}

	response = requests.post(baseUrl, json=data, headers=headers)

	print(response.text)

def add_question(apiToken, dataCenter, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions"\
	.format(dataCenter, surveyId)
	
	data = {
		"QuestionText": "<span style=\"color: rgb(0, 0, 0); font-family: docs-Calibri; font-size: 16px; white-space: pre-wrap;\">Hourly Wage:</span>",
            "DataExportTag": "Q1",
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
               "11": {
                  "Display": "$19"
               },
               "13": {
                  "Display": "$20"
               },
               "14": {
                  "Display": "$21"
               },
               "15": {
                  "Display": "$22"
               },
               "16": {
                  "Display": "$23"
               },
               "17": {
                  "Display": "$24"
               },
               "18": {
                  "Display": "$25"
               }
            },
            "ChoiceOrder": [
               1,
               2,
               3,
               "11",
               "13",
               "14",
               "15",
               "16",
               "17",
               "18"
            ],
            "Validation": {
               "Settings": {
                  "ForceResponse": "OFF",
                  "ForceResponseType": "ON",
                  "Type": "None"
               }
            },
            "Language": [],
            "NextChoiceId": 19,
            "NextAnswerId": 1,
            "QuestionID": "QID1",
            "DataVisibility": {
               "Private": False,
               "Hidden": False
            },
            "QuestionText_Unsafe": "<span style=\"color: rgb(0, 0, 0); font-family: docs-Calibri; font-size: 16px; white-space: pre-wrap;\">Hourly Wage:</span>"
         }

	headers = {
   'accept': "application/json",
   'content-type': "application/json",
   "x-api-token": apiToken,
	}

	response = requests.post(baseUrl, json=data, headers=headers)

	print(response.text)

def publish_survey(apiToken, dataCenter, surveyId):
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

def upload_image(dataCenter, apiToken, image_dir):

	baseUrl = "https://{0}.qualtrics.com/API/v3/libraries/UR_2oCfkV4WwzhNcih/graphics".format(dataCenter)
	data = {'file': ('Testing', open(image_dir,'rb'), 'image/jpeg')}
 
	headers = {
	"x-api-token": apiToken}

	response = requests.post(baseUrl, headers=headers, files=data)
	values = json.loads(response.text)
	return values['result']['id']

def upload_all_images(dataCenter, apiToken):
	data = [['Image Folder', 'Image ID']]
	for f in os.listdir('Images'):
		images = os.listdir('Images/' + f)
		image_dir = 'Images/' + f + '/' + str(images[0])
		image_id = upload_image(dataCenter, apiToken, image_dir)
		data.append([f, image_id])
	write_to_spreadsheet(data)



if __name__ == '__main__':
	upload_all_images(dataCenter, apiToken)
	survey_creation(dataCenter, apiToken)
	update_survey(apiToken, dataCenter, 'SV_em75DIWx0q4Ze4d')
	add_question(apiToken, dataCenter, 'SV_em75DIWx0q4Ze4d')
	add_image(apiToken, dataCenter, 'SV_em75DIWx0q4Ze4d')
	add_question(apiToken, dataCenter, 'SV_em75DIWx0q4Ze4d')
	publish_survey(apiToken, dataCenter, 'SV_em75DIWx0q4Ze4d')
	activate_survey(apiToken, dataCenter, 'SV_em75DIWx0q4Ze4d')
	#get_survey_def(apiToken, dataCenter, 'SV_em75DIWx0q4Ze4d')
























