from .HindustanTimes import getData as ht
import random

def getAuto():
    auto = ht()
    random.shuffle(auto)
    return auto

# print(len(getAuto())
