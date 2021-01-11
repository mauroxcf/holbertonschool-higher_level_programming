#!/usr/bin/python3
# sends a POST request to a URL with a parameter using request module
""" Using Request module """


if __name__ == '__main__':
    import sys
    import requests as reqs

    response = reqs.get(sys.argv[1])

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
