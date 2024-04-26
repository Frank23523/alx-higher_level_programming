#!/usr/bin/python3
"""6-peak.py"""


def find_peak(list_of_integers):
	"""finds a peak in a list of unsorted integers"""
	if list_of_integers == None:
		return None
	
	left = 0
	right = len(list_of_integers) - 1

	while left < right:
		middle = (left + right) // 2
		if list_of_integers[middle] < list_of_integers[middle + 1]:
			left = middle + 1
		else:
			right = middle
	
	return list_of_integers[left]
