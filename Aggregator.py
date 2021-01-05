from AllCategories import allcategories as al
from Science import science as sci
from Technology import technology as tech
from Gaming import gaming as game
from Automobile import automobile as auto
from Sports import sports
import random

_allCat = al.getAll()

def getScience():
    science = al.getScience() + sci.getScience()
    random.shuffle(science)
    return science
def getTech():
    techn = al.getTech() + tech.getTech()
    random.shuffle(techn)
    return techn
def getEntertainment():
    return al.getEntertainment()
def getBusiness():
    return al.getBusiness()
def getCulture():
    return al.getCulture()
def getIndia():
    return al.getIndia()
def getAuto():
    return auto.getAuto()
def getSports():
    return sports.getSports()
def getGaming():
    return game.getGame()
def getAll():
    allcats =_allCat()+ getScience()+getTech()+getAuto()+getSports()+getGaming()
    random.shuffle(allcats)
    return allcats

'''

Available Categories Are

Technology

Science

Entertainment

Business

Culture

India

Auto

Sports

Gaming

'''
