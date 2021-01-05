from .GSMArena import getData as gsm
from .TechRadar import getData as tr
from .TechCrunch import getData as tc

def getTech():
    tech = gsm()+tr()+tc()
    return tech.shuffle()

# print(len(getTech()))
