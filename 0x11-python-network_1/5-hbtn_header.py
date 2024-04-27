#!/usr/bin/python3
"""5-hbtn_header.py"""
import requests
from sys import argv


if __name__ == "__main__":
	"""
	takes in a URL, sends a request to the URL and
	displays the value of the variable X-Request-Id
	in the response header
	"""
	response = requests.get(argv[1])
	response_h = response.headers.get('X-Request-Id')
	print(response_h)
