import json

def read_json_as_dict(file_name: str) -> dict:
    with open(file_name) as f:
        contents = "".join(f.readlines())
    return json.loads(contents)


