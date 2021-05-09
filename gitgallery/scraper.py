#!/usr/bin/env python3
# scraper.py
import json

import requests
from requests.exceptions import HTTPError

BASE_URL = "https://api.github.com/users"


def scraper(username: str = '') -> str:
    try:
        responce = requests.get(f'{BASE_URL}/{username}')
        responce.raise_for_status()
        js = json.loads(responce.text)
        _id = js.get('id')
        return _id
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"HTTP error occurred: {e}")
    else:
        print(f"Success! {username}")


if __name__ == "__main__":
    print(scraper("coderj001"))
