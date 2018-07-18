import behave
import requests
import json


@step('a lock X is registered')
def step_registerBike(context):

    API_ENDPOINT = ('https://webservices-solqav.devops.8d.com:8463/api/RegisterOmniSmartBike')

    head = {'Authorization': 'EDT1 ApiKey=cGFydG5lck5hbWVRQTpwYXJ0bmVyUGFzc3dvcmRRQQ==',
            'Content-type': 'application/json'}

    body = {
        "imei" : "444656930830925",
        "displayNumber" : "33333"
    }

    response = requests.post(url=API_ENDPOINT, headers=head, json=body)

    assert response.status_code == 200