from .cricketworld import getData as cw
from .firstpost import getData as fl
import random 

def getSports():
    sports = cw()+fl()
    random.shuffle(sports)
    return sports

# print(len(getSports()))
