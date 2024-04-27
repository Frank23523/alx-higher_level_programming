#!/usr/bin/python3
"""1-hbtn_header.py"""
import urllib.request
from sys import argv


if __name__ == "__main__":
	with urllib.request.urlopen(argv[1]) as response:
		"""
		displays the value of the X-Request-Id variable found
		in the header of the response
		"""
		header = response.getheader('X-Request-Id')
		print(header)
