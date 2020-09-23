import requests
from bs4 import BeautifulSoup as bs
import re

def getData():

    url = "https://www.cricketworld.com/"

    try:
        r = requests.get(url)
        # print(r.content)
    except Exception as e:
        print(e)
        exit(-1)
    soup = bs(r.content.decode('utf-8'), "lxml")

    regex = re.compile('.*mb link.*')
    dataList = soup.find('div',id = 'carousel_3').findAll("div", class_ = regex)

    BASE_URL = 'https://www.cricketworld.com'
    news = []
    for data in dataList:
        try:
            title = data.find('h3').string
        except BaseException:
            title = ""
        try:
            newsUrl = BASE_URL + data.find('a').get("href")
        except BaseException:
            newsUrl = ""
        try:
            content = data.find('p').string
        except BaseException:
            content = ""
        try:
            imageUrl = data.find('img').get("src")[2:]
        except BaseException:
            imageUrl = ""

        newsData = {
                "title": title,
                "content": content,
                "imageUrl": imageUrl,
                "newsUrl": newsUrl}
        news.append(newsData)
    return news

# from pprint import pprint
# pprint(getData())
