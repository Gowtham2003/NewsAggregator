from .ign import getData as ign
from .pcgamer import getData as pcg
import random

def getGame():
    games = ign()+pcg()
    random.shuffle(games)
    return games

# print(len(getGame()))
