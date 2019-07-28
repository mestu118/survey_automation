# The ID and range of a sample spreadsheet.
RANGE_NAME = 'images'

def write_to_spreadsheet(values, service, SPREADSHEET_ID):
    body = {
        'values':values
    }
    # Call the Sheets API
    sheet = service.spreadsheets().values().update(
        spreadsheetId = SPREADSHEET_ID, range = RANGE_NAME, 
        valueInputOption = 'RAW', body = body).execute()

    print('{0} cells updated.'.format(sheet.get('updatedCells')))
