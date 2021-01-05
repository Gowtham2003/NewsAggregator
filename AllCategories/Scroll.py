import requests
from bs4 import BeautifulSoup as bs

def getScroll(query):

    categories = {
            "science": "https://scroll.in/category/83/science-and-technology",

            "technology": "https://scroll.in/category/83/science-and-technology",

            "world": "https://scroll.in/category/3554/world",
            "culture":"https://scroll.in/category/107/culture",
            "india":"https://scroll.in/category/105/india",
            "entertainment":"https://scroll.in/category/3/film-and-tv",
            "business":"https://scroll.in/category/77/business-and-economy",
            "music":"https://scroll.in/category/4/music",
            "books":"https://scroll.in/category/80/books-and-ideas"
            }

    BASE_URL = categories[query]

    news = []
    try:
        r = requests.get(BASE_URL).content
    except Exception as e:
        print(e)
        exit(-1)

    soup = bs(r,"lxml")

    li_Tags = soup.findAll("li",class_="row-story")

    for data in li_Tags:
        try:
            title = data.h1.text
        except BaseException:
            title = ""
        try:
            newsUrl = data.a.get("href")
        except BaseException:
            newsUrl = ""
        try:
            imageUrl = data.img.get("src")
        except BaseException:
            imageUrl = ""
        try:
            content = data.h2.text
        except BaseException:
            content = ""
            continue


        newsData = {
            "title": title,
            "content": content,
            "imageUrl": imageUrl,
            "newsUrl": newsUrl}
        news.append(newsData)
    return news


def getAllScroll():
    cats = ['science', 'technology', 'world', 'culture', 'india', 'entertainnent', 'business',"music","books"]
    news = []
    for i in cats:
        news+=getScroll(i)
    return news
