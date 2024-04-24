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

def getNumberOfLinesFromFile():
    file = open("info.txt",'r')
    output = file.readlines()
    file.close()
    return len(output)

def calculateHypotenusis(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculateHypotenusis3D(x1, x2, y1, y2, z1, z2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def pythagoreanTheorem(a, b):
    return sqrt(a**2 + b**2)

def strToIntAllPoints2D(shape):
    shape.a[0] = int(shape.a[0])
    shape.a[1] = int(shape.a[1])

    shape.b[0] = int(shape.b[0])
    shape.b[1] = int(shape.b[1])

    shape.c[0] = int(shape.c[0])
    shape.c[1] = int(shape.c[1])

    shape.x[0] = int(shape.x[0])
    shape.x[1] = int(shape.x[1])

def strToIntAllPoints3D(shape):
    shape.a[0] = int(shape.a[0])
    shape.a[1] = int(shape.a[1])
    shape.a[2] = int(shape.a[2])

    shape.b[0] = int(shape.b[0])
    shape.b[1] = int(shape.b[1])
    shape.b[2] = int(shape.b[2])

    shape.c[0] = int(shape.c[0])
    shape.c[1] = int(shape.c[1])
    shape.c[2] = int(shape.c[2])

    shape.d[0] = int(shape.d[0])
    shape.d[1] = int(shape.d[1])
    shape.d[2] = int(shape.d[2])

    shape.x[0] = int(shape.x[0])
    shape.x[1] = int(shape.x[1])
    shape.x[2] = int(shape.x[2])