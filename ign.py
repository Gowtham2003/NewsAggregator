import requests
from bs4 import BeautifulSoup as bs

def getData():
    newsDict = {"data":[]}

    url = "https://in.ign.com/?page=4&ist=broll"

    r = requests.get(url)

    soup = bs(r.content,"lxml")

    articles = soup.findAll("article",{"class":"article NEWS"})

    for article in articles:
        title = article.img.get("alt")
        link = article.a.get("href")
        content = article.p.text
        img = article.img.get("srcset").replace("2x","").replace(" ","").split(",")

        newsObject = {
                "title":title,
                "url":link,
                "content":content,
                "imageUrl":img
                }
        newsDict["data"].append(newsObject)

    return newsDict


print(getData())
