#!/usr/bin/env python3
# scraper.py
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://github.com"


def scraper(username: str = ''):
    req = requests.get(f'{BASE_URL}/{username}')
    soup = BeautifulSoup(req.content, "html.parser")
    img = soup.find(
        'img',
        class_='avatar avatar-user width-full border color-bg-primary',
    )
    return img['src']


if __name__ == "__main__":
    print(scraper("coderj001"))
