#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
# -s to disable the progression display (silent)
# -i for grep case-sensitive
# awk to print second column of each line output
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
