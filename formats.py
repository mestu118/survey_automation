from credentials import *

def getGetHeaders():
   headers = {
       "x-api-token": APITOKEN,
   }
   return headers

def getPostHeaders():
   headers = {
      'accept': "application/json",
      'content-type': "application/json",
      "x-api-token": APITOKEN,
   }
   return headers

def getQuestionFormat():
   FORMAT = {
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
   return FORMAT

def getImageFormat(image_id):
   FORMAT = {
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
   return FORMAT

def getSurveyFormat():
   FORMAT ={"BackButton": "false",
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
   return FORMAT
