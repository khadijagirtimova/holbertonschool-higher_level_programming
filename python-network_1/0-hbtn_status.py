#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib.
"""

import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    data = response.read()
