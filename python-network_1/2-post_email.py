#!/usr/bin/python3
"""
Python script that fetches a URL and displays

"""
import sys
import urllib.request
import urllib.parse

if __name__ = "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")


    with urllib.request.urlopen.(url, data) as response:
        body = response.read()

        print(body.decode("utf-8"))
