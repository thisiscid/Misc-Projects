import json
import os
import utils.logger as logger
import time
from pathlib import Path

FILES_PATH=os.path.abspath(os.path.join(os.path.dirname(__file__), "files", "users.json")) # Path to store file. Expects JSON.
def save_user(new_user, new_pass):
    """Function that saves a new user to a JSON file which is later read. Called by signup.py
    Input:
    new_user: str - The username to be saved.
    new_pass: str - The password to be saved."""
    logger.log(f"Opening {FILES_PATH} and saving new data.")# Will always work since load_user creates if it doesn't exist.
    with open(FILES_PATH, 'r+') as file:
        try:
            file_data = json.load(file)
        except json.JSONDecodeError:
            file_data = {}
        if isinstance(file_data, dict):
            file_data[new_user] = new_pass
        else:
            logger.log(f"File {FILES_PATH} is not a dictionary, it is a {type(file_data)}.", category="ERROR")
            raise ValueError()
        file.seek(0)
        file.truncate()
        json.dump(file_data, file)
def load_user():
    """Function that loads users from """
    if os.path.isfile(FILES_PATH):
        logger.log(f"{FILES_PATH} exists, loading file.")
    else:
        logger.log(f"{FILES_PATH} does not exist, creating file now.")
        Path(FILES_PATH).parent.mkdir(parents=True, exist_ok=True)
        Path(FILES_PATH).touch(exist_ok=True)
    with open(FILES_PATH) as json_file:
        try:
            return json.load(json_file)
        except json.JSONDecodeError:
            return {}


