from .ScienceMag import getData as scimag
from .TheWire_Science import getData as wire
from .physicsworld import getData as phyworld

def getScience():
    science = scimag()+wire()+phyworld()
    return science.shuffle()

# print(len(getScience()))
