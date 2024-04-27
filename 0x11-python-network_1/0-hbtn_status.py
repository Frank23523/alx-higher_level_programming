#!/usr/bin/python3
"""What's my status? #0"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    """fetches https://alx-intranet.hbtn.io/status"""
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(utf8_content))
