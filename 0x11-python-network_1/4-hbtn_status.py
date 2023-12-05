#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
using the requests package.
"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("    - type:", type(response.text))
    print("    - content:", response.text)
