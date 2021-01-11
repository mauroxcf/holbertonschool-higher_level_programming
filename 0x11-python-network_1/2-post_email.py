#!/usr/bin/python3
# sends a POST request to the passed URL with the email as a parameter
""" Using urllib.request module """


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    query = {'email': sys.argv[2]}
    encode_query = urllib.parse.urlencode(query).encode('utf-8')

    with urllib.request.urlopen(url, encode_query) as response:
        print(response.read().decode())
