#!/usr/bin/env bash
# a Bash script that takes in a URL, sends a request to that 
# URL, and displays the size of the body of the response.

url=$1

response_body=$(curl -sI "$url" | awk '/Content-Length/ {print $w}' | tr -d '\r')
length=$(echo "$response_body" | awk '/Content-Length/ {print $2}')

echo "$length"
