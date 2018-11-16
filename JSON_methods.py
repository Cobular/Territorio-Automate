from methods import clean_string, find_slide_id
import random
from string import ascii_letters, digits, Template
import json


def make_savage(tile_name, textbox_reference):
    """ Creates a request that makes a tile savage

    :param tile_name: The name of the tile to do apply the effect to
    :param textbox_reference: The textbox_reference that is used to get the ID of the tile name
    :return make_savage_request: A single-item list that contains a complete request to make a tile savage. Just append it to the main request.
    """

    make_savage_request = [
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
                "objectId": textbox_reference.get(clean_string(tile_name))
            }
        }
    ]
    return make_savage_request


def make_blighted(tile_name, textbox_reference):
    """ Creates a request that makes a tile blighted

    :param tile_name: The name of the tile to do apply the effect to
    :param textbox_reference: The textbox_reference that is used to get the ID of the tile name
    :return make_blighted_request: A single-item list that contains a complete request to make a tile blighted. Just append it to the main request.
    """

    make_blighted_request = [
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
                "objectId": textbox_reference.get(clean_string(tile_name)),
                "textRange": {
                    "type": "ALL"
                },
                "fields": "backgroundColor,fontSize"
            }
        }
    ]
    return make_blighted_request


def make_normal(tile_name, textbox_reference):
    """ Creates a request that makes a tile normal

    :param tile_name: The name of the tile to do apply the effect to
    :param textbox_reference: The textbox_reference that is used to get the ID of the tile name
    :return make_blighted_request: A single-item list that contains a complete request to make a tile normal. Just append it to the main request.
    """
    make_normal_request = [
        {
            "updateTextStyle": {
                "style": {
                    "fontSize": {
                        "unit": "PT",
                        "magnitude": 8
                    }
                },
                "objectId": textbox_reference.get(clean_string(tile_name)),
                "textRange": {
                    "type": "ALL"
                },
                "fields": "*"
            }
        }
    ]
    return make_normal_request


def spawn_pin(slide_page_number, tile_name, spawnpoint_reference, pin_creation_data, requested_slide_values):
    """ Spawns a pin created from the pin_creation_data at the spawnpoint corresponding to the tile name name

    :param slide_page_number: Slide number of the current page to spawn the pins onto
    :param tile_name: Name of the tile that needs to have a pin spawn
    :param spawnpoint_reference: Whole spawnpoint dict created earlier
    :param pin_creation_data: Data for the specific tribe's pin to spawn
    :param requested_slide_values: The whole slide JSON data
    :return reference_pin_creation_dict_priority_final: Returns the ready-to-use request to create a pin. Must be fired first.
    :return reference_pin_creation_dict_secondary_final: Returns the ready-to-use request to add effects to the pin to make it look right.
    """
    try:
        alpha = ascii_letters + digits + "_"
        spawned_pin_id = "".join(random.choice(alpha) for i in range(45))

        reference_pin_creation_dict_priority = [{
            "createShape": {
                "elementProperties": {
                    "pageObjectId": "$pageObjectID",
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
                        "shearX": 0,
                        "shearY": 0,
                        "translateX": "$translateX",
                        "translateY": "$translateY",
                        "unit": "EMU"
                    }
                },
                "objectId": "$objectID",
                "shapeType": "$shapeType"
            }}]
        reference_pin_creation_dict_secondary = [{
            "updateShapeProperties": {
                "fields": "outline,shapeBackgroundFill",
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
                        },
                        "weight": {
                            "magnitude": 2,
                            "unit": "PT"
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
        }]
        reference_pin_creation_dict_priority_template = Template(json.dumps(reference_pin_creation_dict_priority))
        reference_pin_creation_dict_secondary_template = Template(json.dumps(reference_pin_creation_dict_secondary))

        reference_pin_creation_dict_priority_final = reference_pin_creation_dict_priority_template.substitute(
            pageObjectID=find_slide_id(requested_slide_values, slide_page_number),
            objectID=spawned_pin_id,
            translateX=spawnpoint_reference.get(tile_name)[0],
            translateY=spawnpoint_reference.get(tile_name)[1],
            shapeType=pin_creation_data.get("shapeType"))

        reference_pin_creation_dict_secondary_final = reference_pin_creation_dict_secondary_template.substitute(
            objectID=spawned_pin_id,
            outlineFillRed=pin_creation_data.get("outlineFillRed"),
            outlineFillGreen=pin_creation_data.get("outlineFillGreen"),
            outlineFillBlue=pin_creation_data.get("outlineFillBlue"),
            solidFillRed=pin_creation_data.get("solidFillRed"),
            solidFillGreen=pin_creation_data.get("solidFillGreen"),
            solidFillBlue=pin_creation_data.get("solidFillBlue"))

        return json.loads(str(reference_pin_creation_dict_priority_final)), \
               json.loads(reference_pin_creation_dict_secondary_final)
    except TypeError:
        pass
