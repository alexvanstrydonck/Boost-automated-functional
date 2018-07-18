from behave import *
import requests

@step("as a technician, I want to get a list of smart bike controllers")
def step_impl(context):

    API_ENDPOINT = ('https://webservices-solqav.devops.8d.com:8463/api/ListSmartBikeControllers')

    head = {'Authorization': 'EDT1 ApiKey=cGFydG5lck5hbWVRQTpwYXJ0bmVyUGFzc3dvcmRRQQ==',
            'Content-type': 'application/json', 'X-API-Version': '2018-05-09'}

    body = {

        "filters": [

            {
                "type": "STRING_FILTER",
                "name": "imei",
                "value": {
                    "operator": "EQ",
                    "values": [
                        "444656930830925"
                    ]
                }
            }
        ]
    }

    response = requests.post(url=API_ENDPOINT, headers=head, json=body)

    #assert response.status_code == 200
    response_json = response.json()
    print(
        response_json
    )
    context.response = response
    context.controllerId = response_json['smartbikeControllers'][0]['id']