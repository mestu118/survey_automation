from __future__ import print_function
from credentials import *
from write_spreadsheet import *
from read_spreadsheet import * 
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import requests
import sys
import json
from formats import *

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def getValues(response):
	values = json.loads(response.text)
	print(values)
	return values

def get_survey_def(APITOKEN, DATACENTER, surveyId):
	# Setting user Parameters

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}"\
												.format(DATACENTER, surveyId)
	response = requests.get(baseUrl, headers=getGetHeaders())
	getValues(reponse)

def survey_creation(DATACENTER, APITOKEN):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions"\
													.format(DATACENTER)
	data = {
			"SurveyName": "My New Survey",
	        "Language": "EN",
	        "ProjectCategory": "CORE",
	        }

	response = requests.post(baseUrl, json=data, headers=getPostHeaders())
	values = getValues(response)
	return values['result']['DefaultBlockID'], values['result']['SurveyID']

def format_survey(APITOKEN, DATACENTER, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/options"\
										.format(DATACENTER, surveyId)

	data = getSurveyFormat()
	
	response = requests.put(baseUrl, json=data, headers=getPostHeaders())
	getValues(response)

def activate_survey(APITOKEN, DATACENTER, surveyId):
	baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}"\
								.format(DATACENTER, surveyId)

	data = {
	  "isActive": True
	}

	response = requests.put(baseUrl, json=data, headers=getPostHeaders())
	getValues(response)

def add_image(APITOKEN, DATACENTER, surveyId, image_id):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions"\
	.format(DATACENTER, surveyId)
	
	data = getImageFormat(image_id)
	response = requests.post(baseUrl, json=data, headers=getPostHeaders())
	values = getValues(response)
	return values['result']['QuestionID']

def add_question(APITOKEN, DATACENTER, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/questions"\
	.format(DATACENTER, surveyId)
	
	data = getQuestionFormat()

	response = requests.post(baseUrl, json=data, headers=getPostHeaders())
	values = getValues(response)
	return values['result']['QuestionID']

def publish_survey(DATACENTER, APITOKEN, surveyId):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/versions"\
														.format(DATACENTER, surveyId)

	data = {
	  "Description": "2018 New Survey Version",
	  "Published": True
	}

	response = requests.post(baseUrl, json=data, headers=getPostHeaders())

	values = getValues(response)
	return values['result']['metadata']['surveyID']


def delete_images(DATACENTER, APITOKEN, image_id):
	baseUrl = "https://{0}.qualtrics.com/API/v3/libraries/UR_2oCfkV4WwzhNcih/graphics/{1}".format(DATACENTER, image_id)

	response = requests.delete(baseUrl, headers = getGetHeaders())
	getValues(response)


def upload_image(DATACENTER, APITOKEN, image_dir, description):

	baseUrl = "https://{0}.qualtrics.com/API/v3/libraries/UR_2oCfkV4WwzhNcih/graphics".format(DATACENTER)
	file = {'file': (description, open(image_dir,'rb'), 'image/jpeg')}

	response = requests.post(baseUrl, headers=getGetHeaders(), files=file)
	values = getValues(response)
	return values['result']['id']

def upload_all_images(DATACENTER, APITOKEN, service):
	data = [['Image Folder', 'Image ID']]
	for f in os.listdir('Images'):
		images = os.listdir('Images/' + f)
		image_dir = 'Images/' + f + '/' + str(images[0])
		image_id = upload_image(DATACENTER, APITOKEN, image_dir, f)
		data.append([f, image_id])
	write_to_spreadsheet(data, service)

def create_block(DATACENTER, APITOKEN, surveyId):

	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/blocks"\
														.format(DATACENTER, surveyId)
	data = {"Type": "Standard",
	"Description": "My Block Name",
	"Options": {
	"BlockLocking": "false",
	"RandomizeQuestions": "false",
	"BlockVisibility": "Collapsed"}
	}

	response = requests.post(baseUrl, json = data, headers = getPostHeaders())
	values = getValues(response)
	return values['result']['BlockID'], values['result']['FlowID']

def update_block(DATACENTER, APITOKEN, surveyId, blockId, questionIds):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/blocks/{2}"\
														.format(DATACENTER, surveyId, blockId)
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


	response = requests.put(baseUrl, json = data, headers = getPostHeaders())

def delete_block(DATACENTER, APITOKEN, surveyId, blockId):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/blocks/{2}"\
										.format(DATACENTER, surveyId, blockId)
	
	headers = {
	   "x-api-token": APITOKEN
	}

	response = requests.delete(baseUrl, headers = headers)
	print(response.text)


def update_flow(DATACENTER, APITOKEN, surveyId, flows, blocks, defaultId):
	baseUrl = "https://{0}.qualtrics.com/API/v3/survey-definitions/{1}/flow".format(DATACENTER, surveyId)
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

	response = requests.put(baseUrl, json = data, headers = getPostHeaders())
	values = getValues(response)

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
	#upload_all_images(DATACENTER, APITOKEN, service)

	images, questions = read_item_spreadsheet(service)
	imageToId = read_image_spreadsheet(service)
	##Create survey
	defaultBlock, surveyId = survey_creation(DATACENTER, APITOKEN)
	format_survey(APITOKEN, DATACENTER, surveyId)

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
			blockID, flowID = create_block(DATACENTER, APITOKEN, surveyId)
			flows.append(flowID)
			blocks.append(blockID)
			print("adding image")
			ID = add_image(APITOKEN, DATACENTER, surveyId, imageToId[folder])
			questionIDs.append(ID)
			print("adding question")
			ID = add_question(APITOKEN, DATACENTER, surveyId)
			questionIDs.append(ID)
			print("updating block")
			update_block(DATACENTER, APITOKEN, surveyId, blockID, questionIDs)
			counter += 1
		if counter == 3:
			break

	update_flow(DATACENTER, APITOKEN, surveyId, flows, blocks, defaultBlock)
	publish_survey(DATACENTER, APITOKEN, surveyId)
	activate_survey(APITOKEN, DATACENTER, surveyId)
	print("https://nyu.qualtrics.com/jfe/form/{}".format(surveyId))
	# print(surveyId)
	# get_survey_def(apiToken, DATACENTER, surveyId)
























