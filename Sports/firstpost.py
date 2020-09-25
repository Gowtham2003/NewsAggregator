import requests
from bs4 import BeautifulSoup as bs

def getData():
    BASE_URL = "https://www.firstpost.com/firstcricket"

    try:
        r = requests.get(BASE_URL).content

    except Exception as e:
        print(e)
        exit(-1)

    news = []

    soup = bs(r,"lxml")

    divs = soup.findAll("div","image-wrap")
    
    for div in divs:
        try:
            title = div.find("h2",class_="title-text").text.strip()
        except BaseException:
            title = ""
        try:
            newsUrl = div.a.get("href")
        except BaseException:
            newsUrl = ""
        try:
            imageUrl = div.img.get("data-src").replace("//","https://")
        except BaseException:
            imageUrl = ""
        try:
            content = div.find("h4", class_="sub-title-txt").text.strip()
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

print(len(getData()))
