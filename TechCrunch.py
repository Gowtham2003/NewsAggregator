import requests
import json 
from bs4 import BeautifulSoup as bs
import html

def getData():
    url = "https://techcrunch.com/wp-json/tc/v1/magazine?page=1&_embed=true&cachePrevention=0"
    try:
        r = requests.get(url).json()
    except Exception as e:
        print(e)
        exit(-1)

    news = []

    for data in r:
        try:
            encodedTitle = data["title"]["rendered"]
            title = html.unescape(encodedTitle)
        except:
            title = ""
        try:
            contentEncoded = data["excerpt"]["rendered"]
            content = bs(contentEncoded,"lxml").p.text
        except:
            content = ""
        try:
            img = data["jetpack_featured_media_url"]
        except:
            img = ""
        try:
            url = data["shortlink"]
        except:
            url = ""

        newsData = {
                "title":title,
                "content":content,
                "imageUrl":img,
                "newsUrl":url
                }
        news.append(newsData)
    return news


print(getData())
