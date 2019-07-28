# Survey Automation
Survey Automation using Qualtrics API

# Requirements

## Download/Clone repository
## Create Virtual Environment and install dependencies
### Inside repository create environment (e.g. `python -m venv env`)
### Activate environment (e.g. `source env/bin/activate`)
### Install dependencies (e.g. `pip install -r req.txt`)

## Download Image from DropBox repository
### Place inside folder and rename folder 'Images'
### Run `python image_resize.py height(default = 400) width (default = 340_` (will resize all images to corresponding height and width)


## Creating the appropriate credentials 
### Go to Google Cloud Platform and create project through the Console.
### Once project is created go to 'API & Services' then 'Credentials'
### Go to 'OAuth Consent Screen' and set 'Application Name' and save (will essentially give consent)
### Go to 'Credentials' tab select 'Create Credentials', select 'OAuth client ID', select 'Other' and set 'Name' and finally create 
### Under the 'Credentials' tab there should be a new ID, select the Download option at the right side 
### Place the downloaded file in the project folder and rename 'credentials_web.json'

## Enabling Googl Sheets API
### Under APIs & Services select 'Enable APIs and Services'
### Search for 'Google Sheets APIs' and enable

## API Key & Datacenter
### Data Center
Once in your account the data center will be the pre-fix of the link (e.g. https://nyu.ca1.qualtrics.com/ControlPanel/ 'nyu.ca1' is the datacenter)
### API Key
Under the Account Settings go to Qualtrics IDs. Under API, either generate token or copy the Token. 
### Set the appropriate values in credentials.py

## Spreadsheet ID
### Open the Hire Salary on Google Drive and Open as Google Sheets. Then select 'Save as Google Sheets' under 'File'
### Obtain the sheet ID
Can do this by opening the sheet and obtaining the ID from the browser link. For example:
https://docs.google.com/spreadsheets/d/1234ABC/edit
Spreadsheet ID = 123ABC
### Add a sheet named 'images' in the 'Hire Salary' spreadsheet
### Set the appropriate value in credentials.py

## Uploading all images to Qualtrics
### Run `python main.py upload`
### If the web browser prompts you, select the account where the 'Hire Salary' sheet is located and Allow. 


## Create Survey
### Run `python main.py`
### Once survey is created, the survey link will be printed and will be ready to use!


