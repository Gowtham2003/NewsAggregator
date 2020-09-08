import requests
from bs4 import BeautifulSoup as bs

def getData():
    url = "https://www.techradar.com/in/news"
    r = requests.get(url)
    soup = bs(r.content,"lxml")
    dataList = soup.findAll("div",{"data-page":1})
    news = []
    for data in dataList:
        title = data.find("a").get("aria-label")
        title = data.find("h3",class_="article-name").text
        url = data.find("a").get("href")
        content = data.find("p",class_="synopsis").text.replace("Updated","").replace("How to watch","")
        img = data.find("div",class_="image-remove-reflow-container landscape").get("data-original")
        newsData = {                                              "title": title,                                   "content": content,                 
                "imageUrl": img,                    
                "newsUrl": url                                    }
        news.append(newsData)
    return news

print(getData())
