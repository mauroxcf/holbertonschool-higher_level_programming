#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
""" Using urllib.request module """


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as page:
        obt_stat = page.read()
    print("Body response:")
    print("\t- type: {}".format(type(obt_stat)))
    print("\t- content: {}".format(obt_stat))
    print("\t- utf8 content: {}".format(obt_stat.decode()))
