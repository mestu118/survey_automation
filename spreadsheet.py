import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials_gspread.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Questions").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
list_of_hashes = sheet.col_values(1)
col = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
index = 2
sheet.delete_row(index)
print(list_of_hashes)
