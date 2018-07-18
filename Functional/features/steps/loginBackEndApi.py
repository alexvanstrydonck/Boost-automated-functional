import behave
import requests
import json


@step('i m authorized to log in the backEndApi')
def step_loginBackEndApi(context):

    API_ENDPOINT = ('https://webservices-solqav.devops.8d.com:8463/api/v1/LoginUser')

    head = {'Authorization': 'EDT1 ApiKey=cGFydG5lck5hbWVRQTpwYXJ0bmVyUGFzc3dvcmRRQQ==',
            'Content-type': 'application/json'}

    body = {
        "username": "ls",
        "password": "LS1234ls"
    }

    response = requests.post(url=API_ENDPOINT, headers=head, json=body)

    assert response.status_code == 200
    response = response.json()
    print(
        response
    )


@step("I log in the backEndApi")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("i'm authenticated to the backEndApi")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


