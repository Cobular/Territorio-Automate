from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json
import re


def clean_string(string_to_clean):
    return re.sub('[^A-Za-z0-9]+', '', string_to_clean.strip().lower())


def auth():
    """ Signs in to the APIs with the criteria needed to run the program.

    Saves the credentials to storage_main.json

    Returns SLIDES and SHEETS that contain the auth info for the slides API and sheets API
    """
    SCOPES = (
        'https://www.googleapis.com/auth/spreadsheets.readonly',
        'https://www.googleapis.com/auth/presentations'
    )
    store = file.Storage('storage_main.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    HTTP = creds.authorize(Http())
    SLIDES = discovery.build('slides', 'v1', http=HTTP)
    SHEETS = discovery.build('sheets', 'v4', http=HTTP)
    return SLIDES, SHEETS


def download(slides, sheets, sheet_id, presentation_id, data_range):
    """ Downloads the data from the sheet

    :param slides: Slides authentication data from methods.auth()
    :param sheets: Sheets authentication data from methods.auth()
    :param sheet_id: ID for the requested Google Sheet. Can be found in the URL for the sheet
    :param presentation_id: ID for the requested Google Slides presentation. Can be found in the URL for the sheet
    :param data_range: Request a specific range of data to save on processing speed
    :return: Returns the JSON with sheet and slides values
    """
    print('** Fetching Data, may take a bit')
    requestedSheetValues = sheets.spreadsheets().values().get(range=data_range, spreadsheetId=sheet_id,
                                                              majorDimension='ROWS').execute().get('values')
    requestedSlideValues = slides.presentations().get(presentationId=presentation_id).execute().get('slides')
    return requestedSheetValues, requestedSlideValues


def save_data(requestedSlideValues, requestedSheetValues):
    """ Saves the slides abd sheets JSON to the disk for manual review

    :param requestedSlideValues: The JSON for the Google Slide Presentation. Saved as JSON_for_testing/sheetsData_main.json
    :param requestedSheetValues: The JSON for the Google Sheet. Saved as JSON_for_testing/slidesData_main.json
    :return: Nothing
    """
    with open('JSON_for_testing/sheetsData_main.json', 'w') as sheetsDataFile:
        json.dump(requestedSheetValues, sheetsDataFile, indent=4)

    with open('JSON_for_testing/slidesData_main.json', 'w') as slidesDataFile:
        json.dump(requestedSlideValues, slidesDataFile, indent=4)


def create_textbox_reference(requested_slide_values, slide_number):
    """ Creates a dict associating textbox contents to IDs. Will work at both root level and in groups.

    :param requested_slide_values: A Google Slides Presentation JSON to parse.
    :param slide_number: The number of the slide to look at, slide 1 is 0. 0 is recommended.
    :return textbox_reference: A dict of polygon names (cleaned) to textbox IDs
    """
    textbox_reference = {}
    for pageElement in requested_slide_values[slide_number]['pageElements']:
        try:
            # Finds the root level page elements
            for textElement in pageElement['shape']['text']['textElements']:
                try:
                    textbox_reference.update(
                        {clean_string(str(textElement)): clean_string(str(pageElement['objectId']))}
                    )
                except KeyError:
                    pass
        except KeyError:
            pass
        try:
            # Finds the text elements in one level deep groups
            for groupElement in pageElement['elementGroup']['children']:
                try:
                    # Tries to save the text element of the group. Will fail if it's the wrong groupElement.
                    textbox_reference.update(
                        {clean_string(str(groupElement['shape']['text']['textElements'][1]['textRun']['content'])):
                             clean_string(str(groupElement['objectId']))}
                    )
                except KeyError:
                    pass
        except KeyError:
            pass
    return textbox_reference


def create_spawnpoint_reference(requested_slide_values):
    """ Creates the reference dict of tile names to spawnpoints

    :param requested_slide_values: A Google Slides Presentation JSON to parse.
    :return spawnpoint_reference: A dict that associates the tile name and correct spawnpoint.
    """
    spawnpoint_reference = {}

    for pageElement in requested_slide_values[0]['pageElements']:
        shape_name = ""  # Need this variable to have this scope
        line_transform = []  # type: list[int, int]
        try:
            if pageElement['elementGroup'] is not None:
                for groupElement in pageElement['elementGroup']['children']:
                    try:
                        if groupElement['line'] is not None:
                            # Write the transform to a variable that will be used to create the dict in a bit.
                            line_transform = [groupElement['transform']['translateX'],
                                              groupElement['transform']['translateY']]
                    except KeyError:
                        pass
                    try:
                        if groupElement['shape']['text'] is not None:
                            # Saves the name of the shape in the group
                            shape_name = clean_string(
                                str(groupElement['shape']['text']['textElements'][1]['textRun']['content']))
                    except KeyError:
                        pass
        except KeyError:
            pass
        # Actually updates the spawnpoint dict
        spawnpoint_reference.update({shape_name.strip().lower(): line_transform})
    return spawnpoint_reference

