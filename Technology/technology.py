from .GSMArena import getData as gsm
from .TechRadar import getData as tr
from .TechCrunch import getData as tc
from .macworld import getData as mc
import random

def getTech():
    tech = gsm()+tr()+tc()+mc()
    random.shuffle(tech)
    return tech

# print(len(getTech()))
