import requests
from bs4 import BeautifulSoup as bs
# from pprint import pprint

def getData():
    url = "https://www.sciencemag.org/news/latest-news"

    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        exit(-1)
    soup = bs(r.content, "lxml")
    dataList = soup.find('ul',class_ = 'headline-list').findAll("li") 

    BASE_URL = 'https://www.sciencemag.org'
    news = []
    for data in dataList:
        try:
            title = data.find('h2').string.strip()
        except BaseException:
            title = ""
        try:
            newsUrl = BASE_URL + data.find('a').get("href")
        except BaseException:
            newsUrl = ""
        try:
            content = data.find('div',class_ = 'media__deck').string.strip()
        except BaseException:
            content = ""
        try:
            img = data.find('img').get("src")[2:]
        except BaseException:
            img = ""

        newsData = {
                "title": title,
                "content": content,
                "imageUrl": img,
                "newsUrl": newsUrl}
        news.append(newsData)
    return news
# pprint(getData())
