import requests
import json


def jprint(obj):
    """Format and print JSON data."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def main():
    """Retrieve and display current astronaut information."""
    url = "http://api.open-notify.org/astros"

    response = requests.get(url, timeout=10)

    print("Current Astronaut API")
    print("---------------------")
    print("Status Code:", response.status_code)

    print("\nUnformatted Response:")
    print(response.json())

    print("\nFormatted Response:")
    jprint(response.json())


if __name__ == "__main__":
    main()
