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

    # regex = re.compile('excerpt c.*')
    
    dataList = soup.find("div",class_="wp-block-column").findAll("div", {"class": 'item-inner'})

    #findAll('div',class_=regex)
    news = []

    for data in dataList:
        # print(data)
        try:
            title = data.find("h3").text.strip()
        except BaseException:
            title = ""
        try:
            newsUrl = data.find("a").get("href")
            if(not newsUrl.startswith("https://")):
                newsUrl = url + newsUrl
        except BaseException:
            newsUrl = ""
        try:
            content = data.find("span",class_="item-excerpt").text.strip()
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
# print(getData())
