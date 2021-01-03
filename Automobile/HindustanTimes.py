import requests
from bs4 import BeautifulSoup as bs

def getData():
    BASE_URL = "https://auto.hindustantimes.com"

    try:
        r = requests.get(BASE_URL).content

    except Exception as e:
        print(e)
        exit(-1)

    news = []

    soup = bs(r,"lxml")

    section = soup.findAll("section",class_="cardHolder expandObject page-view-candidate")

    for data in section:
        try:
            title = data.find("div", class_="figcaption").text.replace("\n","")
        except BaseException:
            title = ""
        try:
            newsUrl = data.find("meta",{"itemprop":"url"}).get("content")
        except BaseException:
            newsUrl = ""
        try:
            imageUrl = data.img.get("data-src")
        except BaseException:
            imageUrl = ""
        try:
            content = data.find("ul", class_="highlights").text.replace(".","\n")
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
