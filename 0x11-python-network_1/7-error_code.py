#!/usr/bin/python3
"""Error code #1"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL, sends a request to the URL
    and displays the body of the response.
    """
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
