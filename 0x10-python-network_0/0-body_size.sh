#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
# -s to disable the progression display (silent)
# -w specify custom output formatting
# -o to save the body of the resulting response to a file
curl -s -w "%{size_download}" -o /dev/null "$1"
