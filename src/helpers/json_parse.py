import json


def loadJSON(file_path, encoding="utf-8"):
    """
    Load a JSON file from the specified file path.

    This function opens a JSON file, reads its contents, and returns the data
    as a Python dictionary.

    :param file_path: The path to the JSON file to be loaded.
    :param encoding: The file is opened with UTF-8 encoding as default.

    :return: The data contained in the JSON file as a Python dictionary.

    :raises FileNotFoundError: If the specified file does not exist.
    :raises json.JSONDecodeError: If the file is not a valid JSON format.

    """
    with open(file_path, "r", encoding=encoding) as file:
        return json.load(file)
