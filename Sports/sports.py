from cricketworld import getData as cw
from firstpost import getData as fl

def getSports():
    sports = cw()+fl()
    return sports.shuffle()

# print(len(getSports()))
