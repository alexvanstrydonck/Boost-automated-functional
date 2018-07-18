from behave import *
import requests


@given("a controller X exist in the system")
def get_controller(context):

    API_ENDPOINT = ('https://webservices-solqav.devops.8d.com:8463/api/GetSmartBikeController')

    head = {'Authorization': 'EDT1 ApiKey=cGFydG5lck5hbWVRQTpwYXJ0bmVyUGFzc3dvcmRRQQ==',
            'Content-type': 'application/json', 'X-API-Version': '2018-05-09'}

    body = dict({})
    body['id'] = context.controllerId
    #     {
    #     "id": "{context.controllerId}"
    # }

    response = requests.post(url=API_ENDPOINT, headers=head, json=body)

    response_json = response.json()
    print(response_json)
    context.response = response

    assert 'status' in response_json['controller']['lock']
    assert response_json['controller']['lock']['status'] == 'OPEN_AND_LOCKABLE'