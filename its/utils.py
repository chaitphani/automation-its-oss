from its import constants, valut
import json, requests


def header_with_token_generator():

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(constants.TOKEN_URL, data=valut.PAYLOAD, headers=headers, auth=valut.AUTH_DETAILS)

    resp_data = json.loads(response.__dict__["_content"])
    access_token = resp_data["access_token"]

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-type": "application/json",
        "Accept": "application/json",
    }

    return headers
