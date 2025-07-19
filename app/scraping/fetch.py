import requests
from bs4 import BeautifulSoup

class Fetcher:
    @staticmethod
    def fetch_soup(url: str) -> BeautifulSoup:
        response = requests.get(url)
        return BeautifulSoup(response.text, 'lxml')