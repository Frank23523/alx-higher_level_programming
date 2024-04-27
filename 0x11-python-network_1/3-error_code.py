#!/usr/bin/python3
"""3-error_code.py"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
	try:
		with urllib.request.urlopen(argv[1]) as response:
			"""
			takes in a URL, sends a request to the URL and
			displays the body of the response (decoded in utf-8).
			"""
			print(response.read().decode('utf-8'))
	except urllib.error.HTTPError as e:
		print("Error code: {}".format(e.code))
