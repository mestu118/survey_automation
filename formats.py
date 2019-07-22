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

def getLikelihoodQuestionFormat():
   FORMAT =  {
                "ChoiceOrder": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "Choices": {
                    "1": {
                        "Display": "Extremely likely"
                    },
                    "2": {
                        "Display": "Somewhat likely"
                    },
                    "3": {
                        "Display": "Neither likely nor unlikely"
                    },
                    "4": {
                        "Display": "Somewhat unlikely"
                    },
                    "5": {
                        "Display": "Extremely unlikely"
                    }
                },
                "Configuration": {
                    "LabelPosition": "BELOW",
                    "QuestionDescriptionOption": "UseText"
                },
                "DataExportTag": "Q4",
                "DataVisibility": {
                    "Hidden": False,
                    "Private": False
                },
                "Language": [],
                "NextAnswerId": 1,
                "NextChoiceId": 6,
                "QuestionDescription": "How likely are you to hire the following candidate?",
                "QuestionID": "QID4",
                "QuestionText": "How likely are you to hire the following candidate?",
                "QuestionText_Unsafe": "How likely are you to hire the following candidate?",
                "QuestionType": "MC",
                "Selector": "SAHR",
                "SubSelector": "TX",
                "Validation": {
                    "Settings": {
                        "ForceResponse": "OFF",
                        "ForceResponseType": "ON",
                        "Type": "None"
                    }
                  }
               }
   return FORMAT

def getScaleQuestionFormat():
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

def getImageFormat(image_id, version):
   versions = {1 : "You are hiring an Apple specialist for a temporary position.\n \
                     What hourly wage will you offer the following candidate?",
               2 : "You are hiring an Apple specialist for a permanent (long-term) position.\n \
                   What hourly wage will you offer the following candidate?",
               3 : "You are hiring an Apple specialist for a position beginning today.\n \
                  What hourly wage will you offer the following candidate?", 
               4 : "You are hiring an Apple specialist for a position beginning in three months.\n \
                  What hourly wage will you offer the following candidate?", 
               5 : "You are assiting the Apple store manager to hire an Apple specialist.\n \
                  What hourly wage will you recommend the manager to offer the following candidate?" 
               }
   FORMAT = {
            "QuestionText": "{0}".format(versions[int(version)]),
            "DefaultChoices": False,
            "DataExportTag": "Q1",
            "QuestionID": "QID1",
            "QuestionType": "DB",
            "Selector": "GRB",
            "SubSelector": "WTXB",
            "Configuration": {
               "QuestionDescriptionOption": "UseText"
            },
            "QuestionDescription": "{0}".format(versions[int(version)]),
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
            "QuestionText_Unsafe": "{0}".format(versions[int(version)])
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
