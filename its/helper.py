import json


def json_file_reader(file):
    with open(file, encoding="utf-8") as open_file:
        raw_data = json.load(open_file)
    return raw_data
