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
        except BaseException:
            title = ""
        try:
            contentEncoded = data["excerpt"]["rendered"]
            content = bs(contentEncoded, "lxml").p.text
        except BaseException:
            content = ""
        try:
            img = data["jetpack_featured_media_url"]
        except BaseException:
            img = ""
        try:
            newsUrl = data["shortlink"]
        except BaseException:
            newsUrl = ""

        newsData = {
            "title": title,
            "content": content,
            "imageUrl": img,
            "newsUrl": newsUrl
        }
        news.append(newsData)
    return news


# print(getData())
