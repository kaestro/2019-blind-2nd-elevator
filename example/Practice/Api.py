import requests


url = 'http://localhost:8000'

def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token})\
        .json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token},\
        json={'commands': cmds}).json()