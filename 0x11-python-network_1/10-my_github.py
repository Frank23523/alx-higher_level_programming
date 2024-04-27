#!/usr/bin/python3
"""My GitHub!"""
import requests
from sys import argv


if __name__ == "__main__":
	"""
	takes your GitHub credentials (username and password)
	and uses the GitHub API to display your id
	"""
	username = argv[1]
	password = argv[2]
	url = 'https://api.github.com/user'
	response = requests.get(url, auth=(username, password))
	try:
		print(response.json()['id'])
	except:
		pass
