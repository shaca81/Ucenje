import logging
from bs4 import BeautifulSoup
import requests


logger = logging.getLogger("Naslovi")
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('pylogger.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

url = input("Enter a website to extract the URL's from: ")

r = requests.get("http://" + url)

data = r.text

soup = BeautifulSoup(data, "lxml")

for link in soup.find_all('a'):
    # print(link.get('href'))
    logger.info(link.get('href'))
