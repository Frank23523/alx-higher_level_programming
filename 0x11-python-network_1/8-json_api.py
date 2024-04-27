#!/usr/bin/python3
"""Search API"""
import requests
from sys import argv


if __name__ == "__main__":
	"""
	takes in a letter and sends a POST request to
	http://0.0.0.0:5000/search_user with the letter as a parameter.
	"""
	if len(argv) == 1:
		q = ""
	else:
		q = argv[1]
	
	url = 'http://0.0.0.0:5000/search_user'
	data = {"q": q}
	response = requests.post(url, data=data)

	try:
		json_data = response.json()
		if json_data:
			print("[{}] {}".format(json_data['id'], json_data['name']))
		else:
			print("No result")
	except ValueError:
		print("Not a valid JSON")
