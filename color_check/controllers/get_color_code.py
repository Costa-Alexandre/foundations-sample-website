# This file should contain a function called get_color_code().
# This function should take 1 argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json
import logging


def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.

    # log user color
    logging.info(color_name)

    # controlling for upper case and leading/trailing spaces
    try:
        color_name = color_name.lower().strip()
    except AttributeError:
        logging.error("User did not submit a string")
        pass

    try:
        with open('color_check/data/css-color-names.json') as f:
            data = json.load(f)
            color_hex_code = data[color_name]
    except KeyError:
        logging.error("'%s' is not recognized", color_name)
        raise TypeError("Submitted string does't have a match in JSON file")

    return color_hex_code
