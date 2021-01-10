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
def getIndia():
    return getNews('india')
def getEntertainment():
    return getNews('entertainment')
def getBusiness():
    return getNews('business')
def getSports():
    return getNews('sports')
def getPolitics():
    return getNews('Politics')
