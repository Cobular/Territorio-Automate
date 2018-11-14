import json
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# Creates a JSON for all the pins. Has to be updated manually

pinCreationDict = {
    "pluto":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "RECTANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0,
                      "green": 1,
                      "blue": 1
                    }
                  }
                }
              }
            }
          }
        },
    "sylvian":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleX": 0.0531,
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "RECTANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 1,
                      "green": 1,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "builder":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "ELLIPSE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 1,
                      "green": 0,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "amyca":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "ELLIPSE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "objectID",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0,
                      "green": 0,
                      "blue": 1
                    }
                  }
                }
              }
            }
          }
        },
    "crescent":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "ELLIPSE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "objectID",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0,
                      "green": 1,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "seldnac":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0,
                      "green": 1,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "donglathot":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.6,
                      "green": 0,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "sponk":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.6,
                      "green": 0,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "themass":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.79,
                      "green": 0.85,
                      "blue": 0.99
                    }
                  }
                }
              }
            }
          }
        },
    "khappitawlists":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "RECTANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.93,
                      "green": 1,
                      "blue": 0.25
                    }
                  }
                }
              }
            }
          }
        },
    "biggireds":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.8,
                      "green": 0,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "mothertribe":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 1,
                      "green": 0.85,
                      "blue": 0.4
                    }
                  }
                }
              }
            }
          }
        },
    "hejeebs":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 1,
                      "green": 0.6,
                      "blue": 0
                    }
                  }
                }
              }
            }
          }
        },
    "dravon":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "ELLIPSE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.65,
                      "green": 0.3,
                      "blue": 0.47
                    }
                  }
                }
              }
            }
          }
        },
    "hingadingadurgen":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.4,
                      "green": 0.3,
                      "blue": 0.65
                    }
                  }
                }
              }
            }
          }
        },
    "feru-anri":
        {
          "createShape": {
            "elementProperties": {
              "pageObjectId": "{objectID}",
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
                "scaleY": 0.0531,
                "translateX": "{translateX}",
                "translateY": "{translateY}",
                "unit": "EMU"
              }
            },
            "objectId": "{objectID}",
            "shapeType": "TRIANGLE"
          },
          "updateShapeProperties": {
            "fields": "outline,solidFill",
            "objectId": "{objectID}",
            "shapeProperties": {
              "outline": {
                "outlineFill": {
                  "solidFill": {
                    "color": {
                      "rgbColor": {
                        "red": 0,
                        "green": 0,
                        "blue": 0
                      }
                    }
                  }
                }
              },
              "shapeBackgroundFill": {
                "solidFill": {
                  "color": {
                    "rgbColor": {
                      "red": 0.47,
                      "green": 0.56,
                      "blue": 0.61
                    }
                  }
                }
              }
            }
          }
        },
}
print(str(pinCreationDict.get("pluto")))
plutoJSON = pinCreationDict.get("pluto")
plutoJSON_str = json.dumps(plutoJSON).replace("{", "{{").replace("}", "}}")
plutoJSON_str_2 = str(plutoJSON_str).format(objectID="sadfwerfwerf", translateX=5, translateY=6)
# plutoJSON_reloaded = json.loads(plutoJSON_str.strip("\\"))
# print(str(pinCreationDict.get("pluto")).format(objectID="sadfwerfwerf", translateX=5, translateY=6))

with open('JSON_for_testing/pinCreationRequests.json', 'w') as pinCreationJSON:
    json.dump(pinCreationDict, pinCreationJSON, indent=4)
