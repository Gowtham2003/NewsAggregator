import requests
import json 
from bs4 import BeautifulSoup as bs
import html

url = "https://techcrunch.com/wp-json/tc/v1/magazine?page=1&_embed=true&cachePrevention=0"

r = requests.get(url).json()

news = []

for data in r:
    encodedTitle = data["title"]["rendered"]
    title = html.unescape(encodedTitle)
    contentEncoded = data["excerpt"]["rendered"]
    content = bs(contentEncoded,"lxml").p.text
    img = data["jetpack_featured_media_url"]
    url = data["shortlink"]

    newsData = {
            "title":title,
            "content":content,
            "imageUrl":img,
            "newsUrl":url
            }
    news.append(newsData)

print(news)
