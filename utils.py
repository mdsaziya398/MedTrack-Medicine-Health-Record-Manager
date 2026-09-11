import json
import os


def create_data_folder():
    os.makedirs("data", exist_ok=True)


def load_data(filename):

    create_data_folder()

    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_data(filename, data):

    create_data_folder()

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError:
        return False