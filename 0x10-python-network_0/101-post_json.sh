#!/bin/bash

url="$1"
filename="$2"

json_data=$(cat "$filename")

curl -X POST \
  -H "Content-Type: application/json" \
  -d "$json_data" \
  "$url"

