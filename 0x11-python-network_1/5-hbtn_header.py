#!/usr/bin/python3
# sends a request to the URL and displays X-Request-Id using request module
""" Using Request module """


if __name__ == '__main__':
    import sys
    import requests as reqs

    response = reqs.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
