#!/usr/bin/python3
"""POST an email #0"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter, and displays
    the body of the response (decoded in utf-8)
    """
    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    r = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(r) as response:
        print(response.read().decode('utf-8'))
