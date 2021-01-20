import requests
from bs4 import BeautifulSoup as bs
import re

def getData():
    url = "https://www.macworld.com"
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        exit(-1)
    soup = bs(r.text, "lxml")

    regex = re.compile('excerpt c.*')
    dataList = soup.find("div", {"id": 'home-main-primary'}).findAll('div',class_=regex)
    news = []

    for data in dataList:
        # print(data)
        try:
            title = data.find("p", class_="crawl-headline").text.strip()
        except BaseException:
            title = ""
        try:
            newsUrl = url + data.find("a").get("href")
        except BaseException:
            newsUrl = ""
        try:
            content = data.find("p",class_="crawl-summary").text.strip()
        except BaseException:
            content = ""

        try:
            img = data.find('img').get('src')
        except BaseException:
            img = ""

        newsData = {
                "title": title,
                "content": content,
                "imageUrl": img,
                "newsUrl": newsUrl}
        news.append(newsData)
    return news

# getData()
# print(len(getData()))
