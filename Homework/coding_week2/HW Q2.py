from math import pi

def areaCylinder (radius, length):
    
    area = radius * radius * pi
    
    volume = area * length
    
    return (area, volume)
    