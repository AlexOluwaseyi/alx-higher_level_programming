#!/bin/bash
# Use curl to make a request to 0.0.0.0:5000/catch_me
curl -s 0.0.0.0:5000/catch_me_2 -X PUT -L --data "user_id=98" -H "Origin: School"
