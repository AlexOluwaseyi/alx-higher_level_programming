#!/bin/bash
# a Bash script that sends a JSON POST request to a URL and displays the body of the response.
curl -X POST -H "Content-Type: application/json" -d "$(cat "$2")" -s "$1"
