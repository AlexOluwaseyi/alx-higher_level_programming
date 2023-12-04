#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
echo -n "$(curl -s -o /dev/null -w "%{http_code}" "$1" | tr -d '\n\r')"
