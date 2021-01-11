#!/usr/bin/python3
""" Using Request module """


import requests


if __name__ == '__main__':
    import sys
    import requests as reqs
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    data = {'username': username, 'token': token}
    response = reqs.get(url, auth=(username, token)).json()
    try:
        print(response['id'])
    except:
        print('None')
