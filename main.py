#!./venv/bin python
""" Provides a bunch of automation functions to be used with the game Territorio

My game is hosted at SMHS by Mr. Terril.
For this code to do anything other than crash,
it requires the correct spreadsheet in the sheetID and presentationID fields.
"""

from __future__ import print_function

from typing import Dict
import JSON_methods
import methods

# <editor-fold desc="Author Data">
__author__ = "Jacob Cover"
__credits__ = ["Jacob Cover"]
__license__ = "GPL"
__version__ = "1.2.1"
__maintainer__ = "Jacob Cover"
__email__ = "coverj715+territorio@gmail.com"
# </editor-fold>

# <editor-fold desc="Variable Definitions">
# Creates the dict that will act as the reference in later parts of the code
# tile_name: objectID
textbox_reference = {}  # type: Dict[str, str]
# Creates a dict that will store the spawnpoints for the tiles.
# tile_name: [line_x,line_y]
spawnpoint_reference = {}
# Creates a dict to store the unchanging pin data. Filled out at program-time.
pinSpecReference = {
    'plutos': {
        "shapeType": "RECTANGLE",
        "outlineFillRed": "0",
        "outlineFillBlue": "0",
        "outlineFillGreen": "0",
        "solidFillRed": "0",
        "solidFillBlue": "1",
        "solidFillGreen": "1"
    }
}
# Creates an empty list that all requests will be added to in order toreduce the number of requests sent.
# I was actually hitting the cap! This will do one request per file run with the current setup.
# Filled with tons of JSON stuff
requests_primary = []
requests_secondary = []
# Stores the ID of the sheet to get the data from
sheetID = '11iqzZM2B5nW4ShogiWC-n4_kNV9G6E-sJbk25WgRz58'
# Stores the ID of the presentation to apply the effects to
presentationID = '1QFH68wLkhyfVag4c2JJ1tcEhgSIXhP5W0x-4vRbRrNY'
# Stores the range of the data from the sheet to process here. Currently only works for one sheet tab at a time
dataRange = 'A2:AE373'
# </editor-fold>

# Authenticate with the google APIs
SLIDES, SHEETS = methods.auth()

# Actually get the sheet and slides values data from the API. Returns a JSON file for each one.
requestedSheetValues, requestedSlideValues = methods.download(SLIDES, SHEETS, sheetID, presentationID, dataRange)

# Save the collected JSON values to disk for manual inspection. Mostly for dev & troubleshooting
methods.save_data(requestedSlideValues, requestedSheetValues)

# This iterates over the list of page elements and only adds elements that have a text component to the
# textbox_reference dict, which will be compared to the spreadsheet later
textbox_reference = methods.create_textbox_reference(requestedSlideValues, 0)
print(textbox_reference)

# This iterates over the list of page elements
# and only adds the coordinates of the a line in an element group with a line and a shape in it
spawnpoint_reference = methods.create_spawnpoint_reference(requestedSlideValues)
print(spawnpoint_reference)

for row_dirty in requestedSheetValues:
    # Sets to false if any effect is applied to the tile's text. Only used for text color stuff.
    text_default = True

    # Cleans all the row values to keep them from being problematic
    row = []
    for i in row_dirty:
        row.append(methods.clean_string(i))

    # Check to make sure that name of the row corresponds to an ID TODO: Make sure all elements on the slide have an ID!
    if textbox_reference.get(str(row[0]).strip().lower()) is not None:

        # Control blighted tiles
        if row[5] == 'Blighted':
            # Something changed, so the tile no longer needs to be set to no effects
            text_default = False
            # The actual request body. Just keep this minimized
            requests_primary.append(JSON_methods.make_savage(row[0], textbox_reference))

        # Apply the savage effect
        if row[4] == "Savage":
            # Something changed, so the tile no longer needs to be set to no effects
            text_default = False
            # The actual request body. Just keep this minimized
            requests_primary.append(JSON_methods.make_blighted(row[0], textbox_reference))

        # Reset tiles with no effects to normal. Only runs when no tile effect is applied
        if text_default:
            # The actual request body. Just keep this minimized
            requests_primary.append(JSON_methods.make_normal(row[0], textbox_reference))

        # Spawns pins based on the input
        try:
            requests_primary_temp, requests_secondary_temp = JSON_methods.spawn_pin(0, row[0], spawnpoint_reference,
                                                           pinSpecReference[row[10]], requestedSlideValues)
            requests_primary.append(requests_primary_temp)
            requests_secondary.append(requests_secondary_temp)
            print("Pin spawned: " + row[0])
        except (KeyError, TypeError):
            pass
    else:
        # Just here for debugging, not critical. TODO: Change this to python logging
        print("Row without textbox of name: " + row[0])

# Finally send the one huge request for the primary requests
body = {
    'requests': requests_primary
}

response_primary = SLIDES.presentations().batchUpdate(presentationId=presentationID, body=body).execute()

if requests_secondary.__len__() != 0:
    # Send the secondary requests, if any
    body = {
        'requests': requests_secondary
    }
    response_secondary = SLIDES.presentations().batchUpdate(presentationId=presentationID, body=body).execute()
