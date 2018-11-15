import methods


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
                "objectId": str(textbox_reference.get(methods.clean_string(str(tile_name))))
            }
        }
    ]
    return make_savage_request


def make_
