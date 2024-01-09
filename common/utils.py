import json
import hashlib

def requestBody2Json(request) -> dict:
    body = request.body
    try:
        json_data = json.loads(body)
    except Exception as e:
        raise e
    return json_data


def getFileMd5(file) -> str:
    md5 = hashlib.md5()
    while True:
        data = file.read(1024 * 1024)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()