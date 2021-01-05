from .GSMArena import getData as gsm
from .TechRadar import getData as tr
from .TechCrunch import getData as tc
import random

def getTech():
    tech = gsm()+tr()+tc()
    random.shuffle(tech)
    return tech

# print(len(getTech()))
