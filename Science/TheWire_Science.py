import requests
from bs4 import BeautifulSoup as bs


def getData():
    news = []

    URL = "https://science.thewire.in/latest/"

    try:
        r = requests.get(URL)

    except Exception as e:
        print(e)
        exit(-1)

    soup = bs(r.content, "lxml")

    div = soup.findAll("div", {"class": "small-12 medium-4 columns"})
    for data in div:
        try:
            title = data.find("div", class_="post-title").text
        except BaseException:
            title = ""
        try:
            newsUrl = data.find("div", class_="post-title").a.get('href')
        except BaseException:
            newsUrl = ""
        try:
            imageUrl = data.find("div").figure.a.img.get("src")
        except BaseException:
            imageUrl = ""
        try:
            content = data.find("div").p.text
        except BaseException:
            content = ""

        newsData = {
            "title": title,
            "content": content,
            "imageUrl": imageUrl,
            "newsUrl": newsUrl
        }
        news.append(newsData)
    return news


# print(getData())
