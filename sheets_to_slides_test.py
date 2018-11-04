from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json


# User defined variables
sheetID = '1e8kHX4WTiOcxU_BPcIgjcSjcmVhkzLBITtXVyGZJ8lU'  # <--- Put the id of the sheet there
presentationID = '1QFH68wLkhyfVag4c2JJ1tcEhgSIXhP5W0x-4vRbRrNY'  # <--- Put the id of the presentation
dataRange = 'A2:E4'  # <--- Put the range of the data to process here. Currently only works for one sheet tab at a time


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

# Actually get the sheet and slides values data from the API. Returns a JSON file for each one.
print('** Fetching Data, may take a bit')
requestedSheetValues = SHEETS.spreadsheets().values().get(range=dataRange,
                                                          spreadsheetId=sheetID).execute().get('values')
slideValuesTest = SLIDES.presentations().get(presentationId=presentationID).execute().get('slides')



counter = 0
for textboxes in slideValuesTest[0]['pageElements']:
    #if not textboxes['shape']:
  #      print("Not a shape!")
  #  else:
    try:
        print(textboxes['shape']['text']['textElements'][1]['textRun']['content'])
        print(textboxes['objectId'])
        counter += 1
    except KeyError as error:
        print('Not a Shape! ' + str(error))

print(counter)
