#!/usr/bin/python3
# sends POST request to the URL and displays the body of the response
""" Using urllib.request module """


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse
    from urllib.error import HTTPError
    from urllib.error import URLError

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        page = response.read()
        print(page.decode())

    except HTTPError as err:
        print("Error code: {}".format(err.code))
    except URLError as err:
        print("Error code: {}".format(err.code))
    else:
        pass
