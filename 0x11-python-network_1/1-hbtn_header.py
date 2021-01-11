#!/usr/bin/python3
# displays the value of the X-Request-Id variable using urllib.request
""" Using urllib.request module """


if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as page:
        obt_extract = page.read()
    headers = page.info()
    print(headers['X-Request-Id'])
