#Coded by Sumanjay on 29th Feb 2020
# Copied From http://github.com/cyberboysumanjay/Inshorts-News-API/

import requests
from bs4 import BeautifulSoup
import time

def getNews(category):
    newsList = [] 

    try:
        if category!='all':
            htmlBody = requests.get('https://www.inshorts.com/en/read/' + category)
        else:
            htmlBody = requests.get('https://www.inshorts.com/en/read/')

    except requests.exceptions.RequestException as e:
        return newsList

    soup = BeautifulSoup(htmlBody.text, 'lxml')
    newsCards = soup.find_all(class_='news-card')
    if not newsCards:
        return newsList

    for index,card in enumerate(newsCards):

        try:
            title = card.find(class_='news-card-title').find('a').text.strip()
        except AttributeError:
            title = None

        try:
            imageUrl = card.find(
                class_='news-card-image')['style'].split("'")[1]
        except AttributeError:
            imageUrl = None

        try:
            content = card.find(class_='news-card-content').find('div').text
        except AttributeError:
            content = None

        try:
            readMoreUrl = card.find(class_='read-more').find('a').get('href')
        except AttributeError:
            readMoreUrl = None

        newsObject = {
            'title': title,
            'imageUrl': imageUrl,
            'content': content,
            'newsUrl': readMoreUrl
        }

        newsList.append(newsObject)

    return newsList

# print(getNews("science")[0])
