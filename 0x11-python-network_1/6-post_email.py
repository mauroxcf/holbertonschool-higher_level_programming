#!/usr/bin/python3
# sends a POST request to a URL with a parameter using request module
""" Using Request module """


if __name__ == '__main__':
    import sys
    import requests as reqs

    query = {'email': sys.argv[2]}
    response = reqs.post(sys.argv[1], query)
    print(response.text)
