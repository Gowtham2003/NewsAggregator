from .ign import getData as ign
from .pcgamer import getData as pcg

def getGame():
    games = ign()+pcg()
    return games.shuffle()

# print(len(getGame()))
