import requests
from bs4 import BeautifulSoup as bs


def getData():
    news = []
    url = "https://in.ign.com/?page=1&ist=broll"
    try:
        r = requests.get(url)
    except Exception as e:
        print("There's Somekind of Problem")
        exit(-1)

    soup = bs(r.content, "lxml")
    try:
        articles = soup.findAll("article", {"class": "article NEWS"})
    except Exception as e:
        print(e)
        exit(-1)

    for article in articles:
        try:
            title = article.img.get("alt")
        except BaseException:
            title = ""
        try:
            link = article.a.get("href")
        except BaseException:
            link = ""
        try:
            content = article.p.text
        except BaseException:
            content = ""
        try:
            img = article.img.get("srcset").replace(
                "2x", "").replace(" ", "").split(",")
        except BaseException:
            img = ""

        newsObject = {
            "title": title,
            "content": content,
            "newsUrl": link,
            "imageUrl": img
        }
        news.append(newsObject)

    return news


print(getData())
