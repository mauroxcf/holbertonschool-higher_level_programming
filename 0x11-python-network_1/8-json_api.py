#!/usr/bin/python3
# sends a POST request to a URL with a parameter using request module
""" Using Request module """


if __name__ == '__main__':
    import sys
    import requests as reqs

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        data = sys.argv[1]
    else:
        data = ""

    query = {'q': data}
    response = reqs.post(url, query)

    try:
        resjson = response.json()
        if resjson == {}:
            print("No result")
        else:
            print("[{}] {}".format(resjson['id'], resjson['name']))
    except ValueError:
        print("Not a valid JSON")
