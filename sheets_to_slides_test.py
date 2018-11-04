from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json

# Assorted Variables
textbox_reference = {}

# User defined variables
sheetID = '1TcS0U8AdKQGcmAO1Hf4S8hrEs7BQ1aRqzOWFCx6o_ok'  # <--- Put the id of the sheet there
presentationID = '1QFH68wLkhyfVag4c2JJ1tcEhgSIXhP5W0x-4vRbRrNY'  # <--- Put the id of the presentation
dataRange = 'A2:I172'  # <--- Put the range of the data to process here. Currently only works for one sheet tab at a time


# A ton of Authentication stuff from here to the next comment. Imporatnt but not very interesting
SCOPES = (
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/presentations'
)
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
HTTP = creds.authorize(Http())
SLIDES = discovery.build('slides', 'v1', http=HTTP)
SHEETS = discovery.build('sheets', 'v4', http=HTTP)

# Actually get the sheet and slides values data from the API. Returns a JSON     file for each one.
print('** Fetching Data, may take a bit')
requestedSheetValues = SHEETS.spreadsheets().values().get(range=dataRange, spreadsheetId=sheetID,
                                                          majorDimension='COLUMNS').execute().get('values')
requestedSlideValues = SLIDES.presentations().get(presentationId=presentationID).execute().get('slides')


# This iterates over the list of page elements and only adds elements that have a text component to the
# textbox_reference dict, which will be compared to the spreadsheet later
for textboxes in requestedSlideValues[0]['pageElements']:
    try:
        textbox_reference.update(
            {textboxes['objectId']: textboxes['shape']['text']['textElements'][1]['textRun']['content']}
        )
    except KeyError:
        pass
print(textbox_reference)

# Iterate over the sheet and
with open('sheetsData.json', 'w') as sheetsDataFile:
    json.dump(requestedSheetValues, sheetsDataFile, indent=4)
