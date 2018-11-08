from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json

# Assorted Variables
# Creates the dict that will act as the reference in later parts of the code
textbox_reference = {}
# Creates a dict that will store tile_name: [line_x,line_y]
spawnpoint_reference = {}
# Creates an empty list to reduce the number of requests sent. I was actually hitting the cap!.
# This will do one request per run
requests = []

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
                                                          majorDimension='ROWS').execute().get('values')
requestedSlideValues = SLIDES.presentations().get(presentationId=presentationID).execute().get('slides')


# This iterates over the list of page elements and only adds elements that have a text component to the
# textbox_reference dict, which will be compared to the spreadsheet later
for textboxes in requestedSlideValues[0]['pageElements']:
    try:
        textbox_reference.update(
            {str(textboxes['shape']['text']['textElements'][1]['textRun']['content']).strip().lower():
             str(textboxes['objectId']).strip().lower()}
        )
    except KeyError:
        pass
print(textbox_reference)

# This iterates over the list of page elements
# and only adds the coordinates of the a line in an element group with a line and a shape in it
for pageElement in requestedSlideValues[0]['pageElements']:
    shapeName = ""
    lineTransform = []
    try:
        if pageElement['elementGroup'] is not None:
            for groupElement in pageElement['elementGroup']['children']:
                try:
                    if groupElement['line'] is not None:
                        # Write the transform to a variable that will be used to create the array in a bit.
                        lineTransform = [groupElement['transform']['translateX'], groupElement['transform']['translateY']]
                except KeyError:
                    pass
                try:
                    if groupElement['shape']['text'] is not None:
                        # Saves the name of the shape in the group
                        shapeName = groupElement['shape']['text']['textElements'][1]['textRun']['content']\
                            .strip().lower()
                except KeyError:
                    pass
                spawnpoint_reference.update({shapeName : lineTransform})
    except KeyError:
        pass
print(spawnpoint_reference)

with open('sheetsData.json', 'w') as sheetsDataFile:
    json.dump(requestedSheetValues, sheetsDataFile, indent=4)

with open('slidesData.json', 'w') as slidesDataFile:
    json.dump(requestedSlideValues, slidesDataFile, indent=4)

# Iterate over the sheet and update the slide to match it.
# Lots of JSON POST request bodies, so it's pretty messy-looking. Just collapse the requests.
for row in requestedSheetValues:
    # Sets to false if anything is set to the tile.
    # If the tile is normal, this stays true and is used to set the tile to default at the end
    default = True

    # Check to make sure that name of the row corresponds to an ID
    if textbox_reference.get(str(row[0]).strip().lower()) is not None:
        # Control blighted tiles
        if row[5] == 'Blighted':
            # Something changed, so the tile no longer needs to be set to no effects
            default = False
            # The actual request body. Just keep this minimized
            requests.append([
                {
                    "updateTextStyle": {
                        "style": {
                            "foregroundColor": {
                                "opaqueColor": {
                                    "rgbColor": {
                                        "blue": 0.76,
                                        "green": 0.482,
                                        "red": 0.194
                                    }
                                }
                            },
                            "fontSize": {
                                "unit": "PT",
                                "magnitude": 8
                            }
                        },
                        "textRange": {
                            "type": "ALL"
                        },
                        "fields": "foregroundColor,fontSize",
                        "objectId": str(textbox_reference.get(str(row[0]).strip().lower())) + ""
                    }
                }
            ])
            print('Made a tile Blighted')

        # Apply the savage effect
        if row[4] == "Savage":
            # Something changed, so the tile no longer needs to be set to no effects
            default = False
            # The actual request body. Just keep this minimized
            requests.append([
                {
                    "updateTextStyle": {
                        "style": {
                            "backgroundColor": {
                                "opaqueColor": {
                                    "rgbColor": {
                                        "red": 0.874,
                                        "green": 0.4,
                                        "blue": 0.4
                                    }
                                }
                            },
                            "fontSize": {
                                "unit": "PT",
                                "magnitude": 8
                            }
                        },
                        "objectId": str(textbox_reference.get(str(row[0]).strip().lower())) + "",
                        "textRange": {
                            "type": "ALL"
                        },
                        "fields": "backgroundColor,fontSize"
                    }
                }
            ])
            print('Made a tile Savage')

        # Reset tiles with no effects to normal. Only runs when no tile effect is applied
        if default:
            # The actual request body. Just keep this minimized
            requests.append([
                {
                    "updateTextStyle": {
                        "style": {
                            "fontSize": {
                                "unit": "PT",
                                "magnitude": 8
                            }
                        },
                        "objectId": str(textbox_reference.get(str(row[0]).strip().lower())) + "",
                        "textRange": {
                            "type": "ALL"
                        },
                        "fields": "*"
                    }
                }
            ])
            print('Removed effects from a tile')

    else:
        # Just here for debugging, not critical. TODO: Change this to python logging
        print('Skipped an item with a null ID')

# Finally send the one huge request
body = {
        'requests': requests
    }
response = SLIDES.presentations().batchUpdate(presentationId=presentationID, body=body).execute()
