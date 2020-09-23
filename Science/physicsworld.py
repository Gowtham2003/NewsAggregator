import requests
from bs4 import BeautifulSoup as bs


def getData():

	BASE_URL = "https://physicsworld.com/l/news"
	headers = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 Pro Build/QQ3A.200605.001)'}
	try:
		r = requests.get(BASE_URL,headers=headers)
		# print(r.content)
	except Exception as e:
		print(e)
		exit(-1)
	soup = bs(r.content, "lxml")

	dataList = soup.find('div',id = 'primary').findAll("article", class_ = 'listing-block')

	news = []
	for data in dataList:
		try:
			title = data.find('b').string
		except BaseException:
			title = ""
		try:
			newsUrl  = data.find('a').get("href")
		except BaseException:
			newsUrl  = ""
		try:
			content = data.find('p').string
		except BaseException:
			content = ""
		try:
			imageUrl = data.find('img').get("src")
		except BaseException:
			imageUrl = ""

		newsData = {
				"title": title,
				"content": content,
				"imageUrl": imageUrl,
				"newsUrl": newsUrl}
		news.append(newsData)
	return news

# from pprint import pprint	
# pprint(getData())
