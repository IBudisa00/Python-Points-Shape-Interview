import math
from math import sqrt

def getInfoFromFile():
    file = open("info.txt",'r')
    output = file.readlines()
    values=[]
    for line in output:
        line = line.strip()
        values.append(line.split(", "))
    file.close()
    return values

def calculateHypotenusis(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def strToIntAllPoints(shape):
    shape.a[0] = int(shape.a[0])
    shape.a[1] = int(shape.a[1])

    shape.b[0] = int(shape.b[0])
    shape.b[1] = int(shape.b[1])

    shape.c[0] = int(shape.c[0])
    shape.c[1] = int(shape.c[1])

    shape.x[0] = int(shape.x[0])
    shape.x[1] = int(shape.x[1])