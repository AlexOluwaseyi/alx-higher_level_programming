#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

url=$1

# Use curl to send a request and store only the status code in a variable
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url" | tr -d '\n\r')

# Display only the status code
echo -n "$status_code"
