import behave
import requests


@step('I want to print the response')

def print_response(context):
    print('le status code est: ' +str(context.response.status_code))
    print('le contenu de la reponse est: '+str(context.response.text))