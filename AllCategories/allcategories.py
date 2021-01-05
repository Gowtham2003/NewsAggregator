from .Scroll import getScroll as scroll
from .Scroll import getAllScroll

def getAll():
    return getAllScroll()

def getScience():
    return scroll('science')
def getTech():
    return scroll('technology')
def getWorld():
    return scroll('world')
def getCulture():
    return scroll('culture')
def getIndia():
    return scroll('india')
def getEntertainment():
    return scroll('entertainment')
def getBusiness():
    return scroll('business')
def getMusic():
    return scroll('music')
def getBooks():
    return scroll('books')
