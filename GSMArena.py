import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


def getData():
    url = "https://www.gsmarena.com/news.php3"
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        exit(-1)
    soup = bs(r.content, "lxml")
    dataList = soup.findAll("div", class_='news-item')

    BASE_URL = 'https://www.gsmarena.com/'
    news = []
    for data in dataList:
        try:
            title = data.find('h3').string
        except BaseException:
            title = ""
        try:
            url = BASE_URL + data.find('a').get("href")
        except BaseException:
            url = ""
        try:
            content = data.find('p').string
        except BaseException:
            content = ""
        try:
            img = data.find('img').get("src")
        except BaseException:
            img = ""

        newsData = {
            "title": title,
            "content": content,
            "imageUrl": img,
            "newsUrl": url}
        news.append(newsData)
    return news


pprint(getData())
