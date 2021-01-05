from .ScienceMag import getData as scimag
from .TheWire_Science import getData as wire
from .physicsworld import getData as phyworld
import random

def getScience():
    science = scimag()+wire()+phyworld()
    random.shuffle(science)
    return science

# print(len(getScience()))
