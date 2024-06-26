#!/usr/bin/python3
"""POST an email #1"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response.
    """
    data = {'email': argv[2]}
    response = requests.post(argv[1], data=data)
    print(response.text)
