#!./venv/bin python
""" Provides a bunch of automation functions to be used with the game Territorio

My game is hosted at SMHS by Mr. Terril.
For this code to do anything other than crash,
it requires the correct spreadsheet in the sheetID and presentationID fields.
"""

from __future__ import print_function

import json
import random
import string
from string import Template
import re
import traceback
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
        "solidFillBluee": "1",
        "solidFillGreen": "1"
    }
}
# Creates an empty list that all requests will be added to in order toreduce the number of requests sent.
# I was actually hitting the cap! This will do one request per file run with the current setup.
# Filled with tons of JSON stuff
requests = []
requests_test = []
# Stores the ID of the sheet to get the data from
sheetID = '11iqzZM2B5nW4ShogiWC-n4_kNV9G6E-sJbk25WgRz58'
# Stores the ID of the presentation to apply the effects to
presentationID = '1QFH68wLkhyfVag4c2JJ1tcEhgSIXhP5W0x-4vRbRrNY'
# Stores the range of the data from the sheet to process here. Currently only works for one sheet tab at a time
dataRange = 'A240:AE240'
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
    """Iterate over the sheet and update the slide to match it
    
    Lots of JSON POST request bodies, so it's pretty messy-looking. Just collapse the requests or the whole thing.
    """

    # Sets to false if any effect is applied to the tile.
    text_default = True

    # Cleans all the row stuff
    row = []
    for i in row_dirty:
        row.append(methods.clean_string(i))

    # Check to make sure that name of the row corresponds to an ID
    if textbox_reference.get(str(row[0]).strip().lower()) is not None:
        # Control blighted tiles
        if row[5] == 'Blighted':
            # Something changed, so the tile no longer needs to be set to no effects
            text_default = False
            # The actual request body. Just keep this minimized
            requests.append(JSON_methods.make_savage(row[0], textbox_reference))

        # Apply the savage effect
        if row[4] == "Savage":
            # Something changed, so the tile no longer needs to be set to no effects
            text_default = False
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
            # print('Made a tile Savage')

        # Reset tiles with no effects to normal. Only runs when no tile effect is applied
        if text_default:
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
            # print('Removed effects from a tile')

        try:
            if row[10] is not "":
                print("row 10 is not none: " + row[10] + ": " + type(row[10]).__name__)
                alpha = string.ascii_letters + string.digits + "_"
                spawnedPinID = "".join(random.choice(alpha) for i in range(50))
                referencePinCreationDict = {
                    "createShape": {
                        "elementProperties": {
                            "pageObjectId": "$objectID",
                            "size": {
                                "height": {
                                    "magnitude": 3000000,
                                    "unit": "EMU"
                                },
                                "width": {
                                    "magnitude": 3000000,
                                    "unit": "EMU"
                                }
                            },
                            "transform": {
                                "scaleX": 0.0532,
                                "scaleY": 0.0532,
                                "translateX": "$translateX",
                                "translateY": "$translateY",
                                "unit": "EMU"
                            }
                        },
                        "objectId": "$objectID",
                        "shapeType": "$shapeType"
                    },
                    "updateShapeProperties": {
                        "fields": "shapeProperties,shapeBackgroundFill",
                        "objectId": "$objectID",
                        "shapeProperties": {
                            "outline": {
                                "outlineFill": {
                                    "solidFill": {
                                        "color": {
                                            "rgbColor": {
                                                "red": "$outlineFillRed",
                                                "green": "$outlineFillGreen",
                                                "blue": "$outlineFillBlue"
                                            }
                                        }
                                    }
                                }
                            },
                            "shapeBackgroundFill": {
                                "solidFill": {
                                    "color": {
                                        "rgbColor": {
                                            "red": "$solidFillRed",
                                            "green": "$solidFillGreen",
                                            "blue": "$solidFillBluee"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                referencePinCreationTemplate = Template(str(referencePinCreationDict))
                tribeName = row[10].strip().lower()
                tileName = row[0].strip().lower()

                try:
                    requests.append([
                        referencePinCreationTemplate.substitute(objectID=spawnedPinID,
                                                                translateX=spawnpoint_reference.get(tileName)[0],
                                                                translateY=spawnpoint_reference.get(tileName)[1],
                                                                shapeType=pinSpecReference.get(tribeName).get(
                                                                    "shapeType"),
                                                                outlineFillRed=pinSpecReference.get(tribeName).get(
                                                                    "outlineFillRed"),
                                                                outlineFillGreen=pinSpecReference.get(tribeName).get(
                                                                    "outlineFillGreen"),
                                                                outlineFillBlue=pinSpecReference.get(tribeName).get(
                                                                    "outlineFillBlue"),
                                                                solidFillRed=pinSpecReference.get(tribeName).get(
                                                                    "solidFillRed"),
                                                                solidFillGreen=pinSpecReference.get(tribeName).get(
                                                                    "solidFillGreen"),
                                                                solidFillBluee=pinSpecReference.get(tribeName).get(
                                                                    "solidFillBluee"))
                    ])
                    print("pinCreationSucess!")
                except Exception as ex:
                    traceback.print_tb(ex.__traceback__)
                    print("PinCreationException" + ex)

                try:
                    print(json.dumps(
                        referencePinCreationTemplate.substitute(objectID=spawnedPinID,
                                                                  translateX=spawnpoint_reference.get(tribeName)[0],
                                                                  translateY=spawnpoint_reference.get(tribeName)[1],
                                                                  shapeType=pinSpecReference.get(tribeName).get(
                                                                      "shapeType"),
                                                                  outlineFillRed=pinSpecReference.get(tribeName).get(
                                                                      "outlineFillRed"),
                                                                  outlineFillGreen=pinSpecReference.get(tribeName).get(
                                                                      "outlineFillGreen"),
                                                                  outlineFillBlue=pinSpecReference.get(tribeName).get(
                                                                      "outlineFillBlue"),
                                                                  solidFillRed=pinSpecReference.get(tribeName).get(
                                                                      "solidFillRed"),
                                                                  solidFillGreen=pinSpecReference.get(tribeName).get(
                                                                      "solidFillGreen"),
                                                                  solidFillBlue=pinSpecReference.get(tribeName).get(
                                                                      "solidFillBlue"))), )
                except:
                    pass
        except Exception as e:
            print(e)

    else:
        # Just here for debugging, not critical. TODO: Change this to python logging
        print("Row without textbox of name: " + row[0])

# Finally send the one huge request
body = {
    'requests': requests
}
response = SLIDES.presentations().batchUpdate(presentationId=presentationID, body=body).execute()
