#!/usr/bin/python3
"""cript that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the respons
packages urllib and sys"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader("X-Request-Id")
            print(x_request_id)
    except urllib.error.HTTPError as e:
        print("Error:", e)
