#!/usr/bin/python3
""" Using Request module """


if __name__ == '__main__':
    import requests as reqs
    from requests.auth import HTTPBasicAuth
    from sys import argv

    repository = argv[1]
    user = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repository)
    response = reqs.get(url).json()
    for i in response[:10]:
        print("{}: {}".format(i.get('sha'),
                              i.get('commit').get('author').get('name')))
