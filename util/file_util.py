import json

def read_json_as_dict(file_name: str) -> dict:
    with open(file_name) as f:
        contents = "".join(f.readlines())
    return json.loads(contents)


# import json
# import os

# def read_json_as_dict(filename):
#     base_dir = os.path.dirname(__file__)
#     file_path = os.path.join(base_dir, "..", filename)
#     file_path = os.path.abspath(file_path)
#     with open(file_path, "r") as f:
#         return json.load(f)



