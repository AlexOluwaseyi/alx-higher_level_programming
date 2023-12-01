#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL,
# follows all redirection and displays the body of the response

url=$1

response=$(curl -sL "$url")

echo "$response"
