#!/usr/bin/env python3
# scraper.py
import json

import requests
from requests.exceptions import HTTPError
from fastapi import HTTPException, status

BASE_URL = "https://api.github.com/users"


def scraper(username: str = '') -> str:
    try:
        responce = requests.get(f'{BASE_URL}/{username}')
        js = json.loads(responce.text)
        _id = js.get('id')
        return _id
    except HTTPError as http_err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"HTTP error occurred: {http_err}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"HTTP error occurred: {e}"
        )
    else:
        print(f"Success! {username}")


if __name__ == "__main__":
    print(scraper("coderj001"))
