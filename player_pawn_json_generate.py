import json
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# User defined variables
presentationID = '1XabSI9SJkLMUmFiGTTVjfbGdj5_kMBHLb-Ey1VNxX6Y'  # <--- Put the id of the presentation

# A ton of Authentication stuff from here to the next comment. Imporatnt but not very interesting
SCOPES = (
    'https://www.googleapis.com/auth/presentations'
)
store = file.Storage('storage_pawnGenerate.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
HTTP = creds.authorize(Http())
SLIDES = discovery.build('slides', 'v1', http=HTTP)

# Actually get the sheet and slides values data from the API. Returns a JSON     file for each one.
print('** Fetching Data, may take a bit')
requestedSlideValues = SLIDES.presentations().get(presentationId=presentationID).execute().get('slides')

with open('JSON_for_testing/slidesData_pawnGenerate.json', 'w') as slidesDataFile:
    json.dump(requestedSlideValues, slidesDataFile, indent=4)