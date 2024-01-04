#!/usr/bin/python3
"""
Module for sending a request to a URL and displaying the response body.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Sends a request to the specified URL and displays the body of the response
    (decoded in utf-8).
    Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
