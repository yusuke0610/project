import requests
from bs4 import BeautifulSoup
import re

def scraping():
    url = 'https://news.yahoo.co.jp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    for elem in elems:
        print(elem.contents[0])
        print(elem.attrs['href'])

scraping()

