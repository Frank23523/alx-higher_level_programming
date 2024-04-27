#!/usr/bin/python3
"""4-hbtn_status.py"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
	"""fetches https://alx-intranet.hbtn.io/status"""
	response = requests.get(url)
	
	print("Body response:")
	print("\t- type: {}".format(type(response.text)))
	print("\t- content: {}".format(response.text))
