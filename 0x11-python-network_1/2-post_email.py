#!/usr/bin/python3

"""
a Python script that takes in a URL and an email, sends a POST request
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    def post_email(url, email):
        """
        Sends a POST request with the provided email to the specified URL.
        Displays the body of the response (decoded in utf-8).
        """
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')

        with urllib.request.urlopen(url, data=data) as response:
            body = response.read().decode('utf-8')
            print(body)

    url = sys.argv[1]
    email = sys.argv[2]

    '''    print("Your email is:", email)'''
    post_email(url, email)
