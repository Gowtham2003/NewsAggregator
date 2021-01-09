# from .Scroll import getScroll as scroll
# from .Scroll import getAllScroll
from .inshorts import getNews

def getAll():
    # return getAllScroll()
    return getNews("all")

def getScience():
    return getNews('science')
def getTech():
    return getNews('technology')
def getWorld():
    return getNews('world')
def getCulture():
    return getNews('culture')
def getIndia():
    return getNews('india')
def getEntertainment():
    return getNews('entertainment')
def getBusiness():
    return getNews('business')
def getMusic():
    return getNews('music')
def getBooks():
    return getNews('books')
