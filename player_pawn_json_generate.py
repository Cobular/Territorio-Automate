import json
from string import Template
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import random
import string

pinCreationDict = {
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
                "scaleX": "$scaleX",
                "scaleY": "$scaleY",
                "translateX": "$translateX",
                "translateY": "$translateY",
                "unit": "EMU"
              }
            },
            "objectId": "$objectID",
            "shapeType": "$shapeType"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
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
                      "red": "=solidFillRed=",
                      "green": "=solidFillGreen=",
                      "blue": "=solidFillBlue="
                    }
                  }
                }
              }
            }
          }
        }

print(str(pinCreationDict))
plutoJSON_template = Template(str(pinCreationDict))
print(plutoJSON_template.safe_substitute(objectID="djbsdfjfdrf"))
# plutoJSON_reloaded = json.loads(plutoJSON_str.strip("\\"))
# print(str(pinCreationDict.get("pluto")).format(objectID="sadfwerfwerf", translateX=5, translateY=6))
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
        "fields": "outline,solidFill",
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
                            "blue": "$solidFillBlue"
                        }
                    }
                }
            }
        }
    }
}
referencePinCreationTemplate = Template(str(referencePinCreationDict))
tribeName = "plutos".strip().lower()
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
pinSpawnpointReference = {
    "plutos": [10000, 2000202]
}


print(referencePinCreationTemplate.substitute(objectID=spawnedPinID,
                                        translateX=pinSpawnpointReference.get(tribeName)[0],
                                        translateY=pinSpawnpointReference.get(tribeName)[1],
                                        shapeType=pinSpecReference.get(tribeName).get("shapeType"),
                                        outlineFillRed=pinSpecReference.get(tribeName).get("outlineFillRed"),
                                        outlineFillGreen=pinSpecReference.get(tribeName).get("outlineFillGreen"),
                                        outlineFillBlue=pinSpecReference.get(tribeName).get("outlineFillBlue"),
                                        solidFillRed=pinSpecReference.get(tribeName).get("solidFillRed"),
                                        solidFillGreen=pinSpecReference.get(tribeName).get("solidFillGreen"),
                                        solidFillBlue=pinSpecReference.get(tribeName).get("solidFillBlue")))
