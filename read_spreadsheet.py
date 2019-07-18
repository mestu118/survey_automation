# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1Vk317VsGxixvB6Eff4mY6_1z8bXIKeqlLVAEnTbnpfM'

def read_image_spreadsheet(service, RANGE_NAME = 'images'):

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    retVal = {}
    if not values:
        print('No data found.')
    else:
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            retVal[row[0]] = row[1]
        return retVal

def read_item_spreadsheet(service, RANGE_NAME = 'item assignment!B2:B'):
    sheet = service.spreadsheets()
    range_names = [
        'item assignment!B2:B',
        'item assignment!BV2:BV'
    ]
    result = sheet.values().batchGet(spreadsheetId = SPREADSHEET_ID,
                                ranges = range_names).execute()
    values = result.get('valueRanges', [])
    return values[0]['values'], values[1]['values']
