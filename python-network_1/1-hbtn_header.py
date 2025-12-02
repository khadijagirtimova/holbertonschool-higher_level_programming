#!/usr/bin/python3
"""
Python script that fetches a URL and displays

"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader("X-Request-Id")
    if x_request_id:
        print(x_request_id)
