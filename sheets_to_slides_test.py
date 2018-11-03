from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# User defined variables
sheetID = '1e8kHX4WTiOcxU_BPcIgjcSjcmVhkzLBITtXVyGZJ8lU'  # <--- Put the id of the sheet there
presentationID = '1QFH68wLkhyfVag4c2JJ1tcEhgSIXhP5W0x-4vRbRrNY'  # <--- Put the id of the presentation
dataRange = 'A2:E4'  # <--- Put the range of the data to process here. Currently only works for one sheet tab at a time


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

print('** Fetching Data, may take a bit')
requestedSheetValues = SHEETS.spreadsheets().values().get(range=dataRange,
                                            spreadsheetId=sheetID).execute().get('values')
slideValuesTest = SLIDES.presentations().get(presentationId=presentationID).execute().get('slides')
print(requestedSheetValues)
print(slideValuesTest[:1])
# for row in requestedSheetValues:
