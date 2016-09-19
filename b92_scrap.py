from bs4 import BeautifulSoup
import requests

b92_article = requests.get('http://www.b92.net/info/vesti/index.php?yyyy=2016&mm=06&dd=26&nav_category=78&nav_id=1147897')
soup = BeautifulSoup(b92_article.text, "lxml")


for article in soup.find_all('div', attrs={"class": "article-header"}):
    print(article.text)
