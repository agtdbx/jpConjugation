import json

def load_json_file(file_path: str) -> dict:
    file = open(file_path)
    file_content = file.read()
    file.close()

    return json.loads(file_content)
