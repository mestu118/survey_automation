# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1Vk317VsGxixvB6Eff4mY6_1z8bXIKeqlLVAEnTbnpfM'
RANGE_NAME = 'images'

def write_to_spreadsheet(values, service):
    body = {
        'values':values
    }
    # Call the Sheets API
    sheet = service.spreadsheets().values().update(
        spreadsheetId = SPREADSHEET_ID, range = RANGE_NAME, 
        valueInputOption = 'RAW', body = body).execute()

    print('{0} cells updated.'.format(sheet.get('updatedCells')))
