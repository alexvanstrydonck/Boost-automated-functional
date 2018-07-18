import behave
import requests


@step('a technician try to unlock this lock X')
def step_techTransfer(context):

    API_ENDPOINT = ('https://webservices-solqav.devops.8d.com:8463/api/UnlockSmartBike')

    head = {'Authorization': 'EDT1 ApiKey=cGFydG5lck5hbWVRQTpwYXJ0bmVyUGFzc3dvcmRRQQ==',
            'Content-type': 'application/json'}

    body = {
        "id": "444656930830925"
    }

    response = requests.post(url=API_ENDPOINT, headers=head, json=body)

    assert response.status_code == 200
    response.json()
    print(response.status_code)
    print(response.json())

@step("the lock X unlocks")
def get_controller_unlock(context):

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

    context.lockstatus = response_json['controller']['lock']['status']

    while context.lockstatus != 'OPEN_AND_LOCKABLE':
        response = requests.post(url=API_ENDPOINT, headers=head, json=body)
        context.lockstatus = response.json()['controller']['lock']['status']

    print('get_controller_unlock: context.lockstatus: ' + context.lockstatus)
