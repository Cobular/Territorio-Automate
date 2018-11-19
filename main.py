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
tribe_pin_data = {
    "amyca": {
        "outlineFillRed": "0",
        "outlineFillGreen": "0.76",
        "outlineFillBlue": "1",
        "solidFillRed": "0",
        "solidFillGreen": "0",
        "solidFillBlue": "1"
    },
    "biggireds": {
        "outlineFillRed": "0",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0",
        "solidFillRed": "0.5",
        "solidFillGreen": "0",
        "solidFillBlue": "0"
    },
    "sprite": {
        "outlineFillRed": "0.22",
        "outlineFillGreen": "1",
        "outlineFillBlue": "0",
        "solidFillRed": "1",
        "solidFillGreen": "1",
        "solidFillBlue": "0"
    },
    "findar": {
        "outlineFillRed": "1",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0",
        "solidFillRed": "1",
        "solidFillGreen": "0.64",
        "solidFillBlue": "0"
    },
    "crescent": {
        "outlineFillRed": "0.5",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0.5",
        "solidFillRed": "0",
        "solidFillGreen": "1",
        "solidFillBlue": "1"
    },
    "donglathot": {
        "outlineFillRed": "0.54",
        "outlineFillGreen": "0.27",
        "outlineFillBlue": "0.27",
        "solidFillRed": "0",
        "solidFillGreen": "0.39",
        "solidFillBlue": "0"
    },
    "dravon": {
        "outlineFillRed": "0",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0",
        "solidFillRed": "1",
        "solidFillGreen": "1",
        "solidFillBlue": "1"
    },

    "estilepico": {
        "outlineFillRed": "0.50",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0.50",
        "solidFillRed": "1",
        "solidFillGreen": "0.70",
        "solidFillBlue": "0"
    },
    "unseelie": {
        "outlineFillRed": "0",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0",
        "solidFillRed": "1",
        "solidFillGreen": "0.75",
        "solidFillBlue": "0.79"
    },
    "fekuanri": {
        "outlineFillRed": "0",
        "outlineFillGreen": "0.65",
        "outlineFillBlue": "0.41",
        "solidFillRed": "1",
        "solidFillGreen": "0.70",
        "solidFillBlue": "0"
    },
    "tenadi": {
        "outlineFillRed": "1",
        "outlineFillGreen": "0.75",
        "outlineFillBlue": "0.79",
        "solidFillRed": "0.5",
        "solidFillGreen": "0",
        "solidFillBlue": "0.5"
    },

    "hejeebs": {
        "outlineFillRed": "0",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0.70",
        "solidFillRed": "0",
        "solidFillGreen": "1",
        "solidFillBlue": "1"
    },
    "themaas": {
        "outlineFillRed": "0",
        "outlineFillGreen": "1",
        "outlineFillBlue": "1",
        "solidFillRed": "1",
        "solidFillGreen": "1",
        "solidFillBlue": "1"
    },
    "sylvan": {
        "outlineFillRed": "0",
        "outlineFillGreen": "0.39",
        "outlineFillBlue": "0",
        "solidFillRed": "0",
        "solidFillGreen": "0.65",
        "solidFillBlue": "0.41"
    },
    "khappitawlists": {
        "outlineFillRed": "0.22",
        "outlineFillGreen": "1",
        "outlineFillBlue": "0",
        "solidFillRed": "1",
        "solidFillGreen": "1",
        "solidFillBlue": "1"
    },
    "subria": {
        "outlineFillRed": "1",
        "outlineFillGreen": "1",
        "outlineFillBlue": "1",
        "solidFillRed": "0",
        "solidFillGreen": "0",
        "solidFillBlue": "0.70"
    },
    "manus": {
        "outlineFillRed": "0.35",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0.35",
        "solidFillRed": "0.50",
        "solidFillGreen": "0",
        "solidFillBlue": "1"
    },
    "sponks": {
        "outlineFillRed": "0.5",
        "outlineFillGreen": "0",
        "outlineFillBlue": "0.5",
        "solidFillRed": "1",
        "solidFillGreen": "0",
        "solidFillBlue": "0"
    },

    "plutos": {
        "outlineFillRed": "1",
        "outlineFillGreen": "1",
        "outlineFillBlue": "1",
        "solidFillRed": "0",
        "solidFillGreen": "1",
        "solidFillBlue": "1"
    },
    "seldnac": {
        "outlineFillRed": "1",
        "outlineFillGreen": "1",
        "outlineFillBlue": "0",
        "solidFillRed": "1",
        "solidFillGreen": "0.75",
        "solidFillBlue": "0.79"
    }
}
# Relates the unit identifier to the shape type
unit_type_data = {
    "hg": "ELLIPSE",
    "fa": "DONUT",
    "he": "ROUND_RECTANGLE",
    "wp": "DIAMOND",
    "wr": "TRIANGLE",
    "fw": "HEXAGON",
    "": "SMILEY_FACE"
}
# Creates an empty list that all requests will be added to in order toreduce the number of requests sent.
# I was actually hitting the cap! This will do one request per file run with the current setup.
# Filled with tons of JSON stuff
requests_primary = []
requests_secondary = []
# Stores the ID of the sheet to get the data from
# Testing spreadsheet: 11iqzZM2B5nW4ShogiWC-n4_kNV9G6E-sJbk25WgRz58
# Master Control: 10QaQy5RrgK0TFek23bgNhkwJP6eX6omhIhqfdRUkJ2E
# Territory-Info: 1ylp5eDzlMvk6-82mY_L_1H9Y_YubZyVD_UZ59Sggh-g
sheetID = '10QaQy5RrgK0TFek23bgNhkwJP6eX6omhIhqfdRUkJ2E'
# Stores the ID of the presentation to apply the effects to
presentationID = '1DEV3loAYLM9QYL9pSDht0IYg0nNS4e1MQtwnkRcBifc'
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
spawnpoint_reference = methods.create_spawnpoint_reference(requestedSlideValues, 0)
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
        if row[5] == 'blighted':
            # Something changed, so the tile no longer needs to be set to no effects
            text_default = False
            # The actual request body. Just keep this minimized
            requests_primary.append(JSON_methods.make_savage(row[0], textbox_reference))
            print("Made Blighted")

        # Apply the savage effect
        if row[4] == "savage":
            # Something changed, so the tile no longer needs to be set to no effects
            text_default = False
            # The actual request body. Just keep this minimized
            requests_primary.append(JSON_methods.make_blighted(row[0], textbox_reference))
            print("Made Savage")

        # Reset tiles with no effects to normal. Only runs when no tile effect is applied
        if text_default:
            # The actual request body. Just keep this minimized
            requests_primary.append(JSON_methods.make_normal(row[0], textbox_reference))
            print("Made Default")

        # Spawns pins based on the input
        try:
            requests_primary_temp, requests_secondary_temp = JSON_methods.spawn_pin(0, row[0], spawnpoint_reference,
                                                                                    tribe_pin_data[row[10]], row[11],
                                                                                    unit_type_data,
                                                                                    requestedSlideValues)
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
