"""
Title: Dog API Program
Author: Verdis Moorer
Assignment: Module 9 - APIs
Description: Connects to the Dog CEO API and displays
the API response in unformatted and formatted JSON.
"""

import requests
import json


def jprint(obj):
    """Print JSON data in a readable format."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def main():
    """Connect to the Dog CEO API and display the response."""

    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url, timeout=10)

    print("Dog CEO API Connection Test")
    print("---------------------------")
    print("Status Code:", response.status_code)

    print("\nUnformatted Response:")
    print(response.json())

    print("\nFormatted Response:")
    jprint(response.json())


if __name__ == "__main__":
    main()
