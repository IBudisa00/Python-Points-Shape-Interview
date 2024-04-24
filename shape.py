import utils
from utils import calculateHypotenusis
from utils import getInfoFromFile
from utils import calculateHypotenusis3D
import math
from math import acos
from math import degrees

class Shape2D:
    def __init__(self):
        self.a = (0,0)
        self.b = (0,0)
        self.c = (0,0)
        self.x = (0,0)
        self.rightAngle = "none"
        self.aSide = 0
        self.bSide = 0
        self.cSide = 0
        self.a, self.b, self.c, self.x = getInfoFromFile()

    def calculateSides(self):
        self.aSide = calculateHypotenusis(self.b[0], self.b[1], self.c[0], self.c[1])
        self.bSide = calculateHypotenusis(self.a[0], self.a[1], self.c[0], self.c[1])
        self.cSide = calculateHypotenusis(self.a[0], self.a[1], self.b[0], self.b[1])

    def calculateAngles(self):
        self.calculateSides()
        alfa = round(degrees(acos((self.bSide**2 + self.cSide**2 - self.aSide**2)/ (2 * self.bSide * self.cSide))), 3)
        if(alfa == 90.0):
            self.rightAngle = "a"
            return
        else:
            beta = round(degrees(acos((self.aSide**2 + self.cSide**2 - self.bSide**2)/ (2 * self.aSide * self.cSide))),3)
            if(beta == 90.0):
                self.rightAngle = "b"
                return
            else:
                if(180 - alfa - beta == 90.0):
                    self.rightAngle = "c"

    def checkShapeType(self):
        self.calculateAngles()
        if(self.rightAngle != "none" and self.checkIfSidesAreEqual() == "square"):
            print("Shape IS square.")
            if(self.checkIfPointXInside()):
                print("X IS inside square.")
            else:
                print("X ISN'T part of square.")
            print(f'Diagonal: {self.calculateDiagonal()}')
        elif(self.rightAngle != "none" and self.checkIfSidesAreEqual() == "rectangle"):
            print("Shape IS rectangle.")
            if(self.checkIfPointXInside()):
                print("X IS inside rectangle.")
            else:
                print("X ISN'T part of rectangle.")
            print(f'Diagonal: {self.calculateDiagonal()}')
        else:
            print("Shape cannot be rectangle, exiting program...")
        
    def checkIfSidesAreEqual(self):
        if(self.aSide == self.bSide or self.aSide == self.cSide or self.bSide == self.cSide):
            return "square"
        else:
            return "rectangle"

    def checkIfPointXInside(self):
        self.calculateAngles()
        if(self.rightAngle == "a"):
            factor1 = (self.a[0] * (self.c[1] - self.a[1]) + (self.x[1] - self.a[1]) * (self.c[0] - self.a[0]) - (self.x[0] * (self.c[1] - self.a[1])))/((self.b[1] - self.a[1]) * (self.c[0] - self.a[0]) - ((self.b[0] - self.a[0]) * (self.c[1] - self.a[1])))
            factor2 = (self.x[1] - self.a[1] - (factor1 * (self.b[1] - self.a[1])))/(self.c[1] - self.a[1])
            factorSum = round(factor1 + factor2, 3)
            if((factor1 >= 0 and factor1 <= 1) and (factor2 >= 0 and factor2 <= 1) and factorSum <= 2):
                return True
            else:
                return False
        elif(self.rightAngle == "b"):
            factor1 = (self.b[0]*(self.c[0] - self.b[0]) + (self.x[1] - self.b[1]) * (self.c[0] - self.b[0]) - (self.x[0] * (self.c[0] - self.b[0])))/((self.a[1] - self.b[1]) * (self.c[0] - self.b[0]) - ((self.a[0] - self.b[0]) * (self.c[0] - self.b[0])))
            factor2 = (self.x[1] - self.b[1] - (factor1 * (self.a[1] - self.b[1])))/(self.c[1] - self.b[1])
            factorSum = round(factor1 + factor2, 3)
            if((factor1 >= 0 and factor1 <= 1) and (factor2 >= 0 and factor2 <= 1) and factorSum <= 2):
                return True
            else:
                return False
        else:
            factor1 = (self.c[0] * (self.b[1] - self.c[1]) + (self.x[1] - self.c[1]) * (self.b[0] - self.c[0]) - (self.x[0] * (self.b[1] - self.c[1])))/((self.a[1] - self.c[1]) * (self.b[0] - self.c[0]) - ((self.a[0]- self.c[0]) * (self.b[1] - self.c[1])))
            factor2 = (self.x[1] - self.c[1] - (factor1 * (self.a[1] - self.c[1])))/(self.b[1] - self.c[1])
            factorSum = round(factor1 + factor2, 3)
            if((factor1 >= 0 and factor1 <= 1) and (factor2 >= 0 and factor2 <= 1) and factorSum <= 2):
                return True
            else:
                return False

    def calculateDiagonal(self):
        if(self.rightAngle == "a"):
            diagonal = self.aSide
        elif(self.rightAngle == "b"):
            diagonal = self.bSide
        else:
            diagonal = self.cSide
        return diagonal

class Shape3D:
    def __init__(self):
        self.a = (0,0,0)
        self.b = (0,0,0)
        self.c = (0,0,0)
        self.d = (0,0,0)
        self.x = (0,0,0)
        self.lastPointOfBase = [0,0,0]
        self.rightAngle = "none"
        self.aSide = 0
        self.bSide = 0
        self.cSide = 0
        self.dSide = 0
        self.pointNotInPlane = "none"
        self.a, self.b, self.c, self.d, self.x = getInfoFromFile()

    def checkIfPointsInSamePlane(self):
        #abc
        result = self.a[0] * (self.c[2] * self.b[1] - self.c[1] * self.b[2]) + self.a[1] * (self.c[0] * self.b[2] - self.c[2] * self.b[0]) + self.a[2] * (self.c[1] * self.b[0] - self.c[0] * self.b[1])
        if(result == 0):
            self.pointNotInPlane = "d"
            return
        #bcd
        result = self.b[0] * (self.d[2] * self.c[1] - self.d[1] * self.c[2]) + self.b[1] * (self.d[0] * self.c[2] - self.d[2] * self.c[0]) + self.b[2] * (self.d[1] * self.c[0] - self.d[0] * self.c[1])
        if(result == 0):
            self.pointNotInPlane = "a"
            return
        #acd
        result = self.a[0] * (self.d[2] * self.c[1] - self.d[1] * self.c[2]) + self.a[1] * (self.d[0] * self.c[2] - self.d[2] * self.c[0]) + self.a[2] * (self.d[1] * self.c[0] - self.d[0] * self.c[1])
        if(result == 0):
            self.pointNotInPlane = "b"
            return
        #abd
        result = self.a[0] * (self.d[2] * self.b[1] - self.d[1] * self.b[2]) + self.a[1] * (self.d[0] * self.b[2] - self.d[2] * self.b[0]) + self.a[2] * (self.d[1] * self.b[0] - self.d[0] * self.b[1])
        if(result == 0):
            self.pointNotInPlane = "c"

    def calculateSides(self):
        for i in range (0,3):
            factor1 = (i + 1) % 3
            factor2 = (i + 2) % 3
            if(self.pointNotInPlane == "a"):
                if(self.b[i] == self.c[i] and self.b[i] == self.d[i]):
                    self.bSide = calculateHypotenusis(self.c[factor1], self.c[factor2], self.d[factor1], self.d[factor2])
                    self.cSide = calculateHypotenusis(self.b[factor1], self.b[factor2], self.d[factor1], self.d[factor2])
                    self.dSide = calculateHypotenusis(self.b[factor1], self.b[factor2], self.c[factor1], self.c[factor2])
                    return
            elif(self.pointNotInPlane == "b"):
                if(self.a[i] == self.c[i] and self.a[i] == self.d[i]):
                    self.aSide = calculateHypotenusis(self.c[factor1], self.c[factor2], self.d[factor1], self.d[factor2])
                    self.cSide = calculateHypotenusis(self.a[factor1], self.a[factor2], self.d[factor1], self.d[factor2])
                    self.dSide = calculateHypotenusis(self.a[factor1], self.a[factor2], self.c[factor1], self.c[factor2])
                    return
            elif(self.pointNotInPlane == "c"):
                if(self.a[i] == self.b[i] and self.a[i] == self.d[i]):
                    self.aSide = calculateHypotenusis(self.b[factor1], self.b[factor2], self.d[factor1], self.d[factor2])
                    self.bSide = calculateHypotenusis(self.a[factor1], self.a[factor2], self.d[factor1], self.d[factor2])
                    self.dSide = calculateHypotenusis(self.a[factor1], self.a[factor2], self.b[factor1], self.b[factor2])
                    return
            elif(self.pointNotInPlane == "d"):
                if(self.a[i] == self.b[i] and self.a[i] == self.c[i]):
                    self.aSide = calculateHypotenusis(self.b[factor1], self.b[factor2], self.c[factor1], self.c[factor2])
                    self.bSide = calculateHypotenusis(self.a[factor1], self.a[factor2], self.c[factor1], self.c[factor2])
                    self.cSide = calculateHypotenusis(self.a[factor1], self.a[factor2], self.b[factor1], self.b[factor2])
                    return
            else:
                print("ERROR - Three points are not in same plain, cannot check if rectangular cuboid can be formed.")
                return

    def calculateAnglesInPlain(self):
        self.calculateSides()
        if(self.pointNotInPlane == "none"):
            return
        if(self.pointNotInPlane == "a"):  
            beta = round(degrees(acos((self.cSide**2 + self.dSide**2 - self.bSide**2)/ (2 * self.cSide * self.dSide))), 3)
            if(beta == 90.0):
                self.rightAngle = "b"
                return
            else:
                gamma = round(degrees(acos((self.bSide**2 + self.dSide**2 - self.cSide**2)/ (2 * self.bSide * self.dSide))),3)
                if(gamma == 90.0):
                    self.rightAngle = "c"
                    return
                else:
                    if(180 - beta - gamma == 90.0):
                        self.rightAngle = "d"
                        return
        elif(self.pointNotInPlane == "b"):  
            alfa = round(degrees(acos((self.cSide**2 + self.dSide**2 - self.aSide**2)/ (2 * self.cSide * self.dSide))), 3)
            if(alfa == 90.0):
                self.rightAngle = "a"
                return
            else:
                gamma = round(degrees(acos((self.aSide**2 + self.dSide**2 - self.cSide**2)/ (2 * self.aSide * self.dSide))),3)
                if(gamma == 90.0):
                    self.rightAngle = "c"
                    return
                else:
                    if(180 - alfa - gamma == 90.0):
                        self.rightAngle = "d"
                        return
        elif(self.pointNotInPlane == "c"):  
            alfa = round(degrees(acos((self.bSide**2 + self.dSide**2 - self.aSide**2)/ (2 * self.bSide * self.dSide))), 3)
            if(alfa == 90.0):
                self.rightAngle = "a"
                return
            else:
                beta = round(degrees(acos((self.aSide**2 + self.dSide**2 - self.bSide**2)/ (2 * self.aSide * self.dSide))),3)
                if(beta == 90.0):
                    self.rightAngle = "b"
                    return
                else:
                    if(180 - alfa - beta == 90.0):
                        self.rightAngle = "d"
                        return
        else:
            alfa = round(degrees(acos((self.bSide**2 + self.cSide**2 - self.aSide**2)/ (2 * self.bSide * self.cSide))), 3)
            if(alfa == 90.0):
                self.rightAngle = "a"
                return
            else:
                beta = round(degrees(acos((self.aSide**2 + self.cSide**2 - self.bSide**2)/ (2 * self.aSide * self.cSide))),3)
                if(beta == 90.0):
                    self.rightAngle = "b"
                    return
                else:
                    if(180 - alfa - beta == 90.0):
                        self.rightAngle = "c"
                        return

    def checkAngleOutsideOfPlain(self):
        if(not self.getLastPointOfBase()):
            if(self.pointNotInPlane == "a"):  
                if((self.a[0] == self.b[0] and self.a[1] == self.b[1]) or (self.a[0] == self.b[0] and self.a[2] == self.b[2]) or (self.a[1] == self.b[1] and self.a[2] == self.b[2])):
                    return True
                elif((self.a[0] == self.c[0] and self.a[1] == self.c[1]) or (self.a[0] == self.c[0] and self.a[2] == self.c[2]) or (self.a[1] == self.c[1] and self.a[2] == self.c[2])):
                    return True
                elif((self.a[0] == self.d[0] and self.a[1] == self.d[1]) or (self.a[0] == self.d[0] and self.a[2] == self.d[2]) or (self.a[1] == self.d[1] and self.a[2] == self.d[2])):
                    return True
                elif((self.a[0] == self.lastPointOfBase[0] and self.a[1] == self.lastPointOfBase[1]) or (self.a[0] == self.lastPointOfBase[0] and self.a[2] == self.lastPointOfBase[2]) or (self.a[1] == self.lastPointOfBase[1] and self.a[2] == self.lastPointOfBase[2])):
                    return True
                else:
                    return False
            elif(self.pointNotInPlane == "b"):  
                if((self.a[0] == self.b[0] and self.a[1] == self.b[1]) or (self.a[0] == self.b[0] and self.a[2] == self.b[2]) or (self.a[1] == self.b[1] and self.a[2] == self.b[2])):
                    return True
                elif((self.b[0] == self.c[0] and self.b[1] == self.c[1]) or (self.b[0] == self.c[0] and self.b[2] == self.c[2]) or (self.b[1] == self.c[1] and self.b[2] == self.c[2])):
                    return True
                elif((self.b[0] == self.d[0] and self.b[1] == self.d[1]) or (self.b[0] == self.d[0] and self.b[2] == self.d[2]) or (self.b[1] == self.d[1] and self.b[2] == self.d[2])):
                    return True
                elif((self.b[0] == self.lastPointOfBase[0] and self.b[1] == self.lastPointOfBase[1]) or (self.b[0] == self.lastPointOfBase[0] and self.b[2] == self.lastPointOfBase[2]) or (self.b[1] == self.lastPointOfBase[1] and self.b[2] == self.lastPointOfBase[2])):
                    return True
                else:
                    return False
            elif(self.pointNotInPlane == "c"):  
                if((self.a[0] == self.c[0] and self.a[1] == self.c[1]) or (self.a[0] == self.c[0] and self.a[2] == self.c[2]) or (self.a[1] == self.c[1] and self.a[2] == self.c[2])):
                    return True
                elif((self.b[0] == self.c[0] and self.b[1] == self.c[1]) or (self.b[0] == self.c[0] and self.b[2] == self.c[2]) or (self.b[1] == self.c[1] and self.b[2] == self.c[2])):
                    return True
                elif((self.c[0] == self.d[0] and self.c[1] == self.d[1]) or (self.c[0] == self.d[0] and self.c[2] == self.d[2]) or (self.c[1] == self.d[1] and self.c[2] == self.d[2])):
                    return True
                elif((self.c[0] == self.lastPointOfBase[0] and self.c[1] == self.lastPointOfBase[1]) or (self.c[0] == self.lastPointOfBase[0] and self.c[2] == self.lastPointOfBase[2]) or (self.c[1] == self.lastPointOfBase[1] and self.c[2] == self.lastPointOfBase[2])):
                    return True
                else:
                    return False
            else:  
                if((self.a[0] == self.d[0] and self.a[1] == self.d[1]) or (self.a[0] == self.d[0] and self.a[2] == self.d[2]) or (self.a[1] == self.d[1] and self.a[2] == self.d[2])):
                    return True
                elif((self.b[0] == self.d[0] and self.b[1] == self.d[1]) or (self.b[0] == self.d[0] and self.b[2] == self.d[2]) or (self.b[1] == self.d[1] and self.b[2] == self.d[2])):
                    return True
                elif((self.c[0] == self.d[0] and self.c[1] == self.d[1]) or (self.c[0] == self.d[0] and self.c[2] == self.d[2]) or (self.c[1] == self.d[1] and self.c[2] == self.d[2])):
                    return True
                elif((self.d[0] == self.lastPointOfBase[0] and self.d[1] == self.lastPointOfBase[1]) or (self.d[0] == self.lastPointOfBase[0] and self.d[2] == self.lastPointOfBase[2]) or (self.d[1] == self.lastPointOfBase[1] and self.d[2] == self.lastPointOfBase[2])):
                    return True
                else:
                    return False
        else:
            return False

    def checkShapeType(self):
        self.checkIfPointsInSamePlane()
        if(self.pointNotInPlane == "none"):
            print("ERROR - All points are in same plain, cannot check if forming rectangular cuboid is possible.")
            return
        self.calculateAnglesInPlain()
        if(self.rightAngle != "none" and self.checkIfSidesAreEqual() and self.checkAngleOutsideOfPlain()):
            print("Shape IS rectangular cuboid.")
        else:
            print("Shape ISN'T rectangular cuboid.")
        self.calculateSpaceDiagonal()

    def getLastPointOfBase(self):
        if(self.pointNotInPlane == "none"):
            print("ERROR - Cannot calculate last point of base, none of points is outside of plane.")
            return False
        if(self.pointNotInPlane == "a"):
            if(self.rightAngle == "b"):
                self.lastPointOfBase[0] = self.b[0] + (self.d[0] - self.b[0]) + (self.c[0] - self.b[0])
                self.lastPointOfBase[1] = self.b[1] + (self.d[1] - self.b[1]) + (self.c[1] - self.b[1])
                self.lastPointOfBase[2] = self.b[2] + (self.d[2] - self.b[2]) + (self.c[2] - self.b[2])
            elif(self.rightAngle == "c"):
                self.lastPointOfBase[0] = self.c[0] + (self.d[0] - self.c[0]) + (self.b[0] - self.c[0])
                self.lastPointOfBase[1] = self.c[1] + (self.d[1] - self.c[1]) + (self.b[1] - self.c[1])
                self.lastPointOfBase[2] = self.c[2] + (self.d[2] - self.c[2]) + (self.b[2] - self.c[2])
            elif(self.rightAngle == "d"):
                self.lastPointOfBase[0] = self.d[0] + (self.b[0] - self.d[0]) + (self.c[0] - self.d[0])
                self.lastPointOfBase[1] = self.d[1] + (self.b[1] - self.d[1]) + (self.c[1] - self.d[1])
                self.lastPointOfBase[2] = self.d[2] + (self.b[2] - self.d[2]) + (self.c[2] - self.d[2])
        elif(self.pointNotInPlane == "b"):
            if(self.rightAngle == "a"):
                self.lastPointOfBase[0] = self.a[0] + (self.d[0] - self.a[0]) + (self.c[0] - self.a[0])
                self.lastPointOfBase[1] = self.a[1] + (self.d[1] - self.a[1]) + (self.c[1] - self.a[1])
                self.lastPointOfBase[1] = self.a[2] + (self.d[2] - self.a[2]) + (self.c[2] - self.a[2])
            elif(self.rightAngle == "c"):
                self.lastPointOfBase[0] = self.c[0] + (self.d[0] - self.c[0]) + (self.b[0] - self.c[0])
                self.lastPointOfBase[1] = self.c[1] + (self.d[1] - self.c[1]) + (self.b[1] - self.c[1])
                self.lastPointOfBase[1] = self.c[2] + (self.d[2] - self.c[2]) + (self.b[2] - self.c[2])
            elif(self.rightAngle == "d"):
                self.lastPointOfBase[0] = self.d[0] + (self.b[0] - self.d[0]) + (self.c[0] - self.d[0])
                self.lastPointOfBase[1] = self.d[1] + (self.b[1] - self.d[1]) + (self.c[1] - self.d[1])
                self.lastPointOfBase[1] = self.d[2] + (self.b[2] - self.d[2]) + (self.c[2] - self.d[2])
        elif(self.pointNotInPlane == "c"):
            if(self.rightAngle == "a"):
                self.lastPointOfBase[0] = self.a[0] + (self.d[0] - self.a[0]) + (self.b[0] - self.a[0])
                self.lastPointOfBase[1] = self.a[1] + (self.d[1] - self.a[1]) + (self.b[1] - self.a[1])
                self.lastPointOfBase[1] = self.a[2] + (self.d[2] - self.a[2]) + (self.b[2] - self.a[2])
            elif(self.rightAngle == "b"):
                self.lastPointOfBase[0] = self.b[0] + (self.d[0] - self.b[0]) + (self.a[0] - self.b[0])
                self.lastPointOfBase[1] = self.b[1] + (self.d[1] - self.b[1]) + (self.a[1] - self.b[1])
                self.lastPointOfBase[1] = self.b[2] + (self.d[2] - self.b[2]) + (self.a[2] - self.b[2])
            elif(self.rightAngle == "d"):
                self.lastPointOfBase[0] = self.d[0] + (self.b[0] - self.d[0]) + (self.c[0] - self.d[0])
                self.lastPointOfBase[1] = self.d[1] + (self.b[1] - self.d[1]) + (self.c[1] - self.d[1])
                self.lastPointOfBase[1] = self.d[2] + (self.b[2] - self.d[2]) + (self.c[2] - self.d[2])
        else:
            if(self.rightAngle == "a"):
                self.lastPointOfBase[0] = self.a[0] + (self.c[0] - self.a[0]) + (self.b[0] - self.a[0])
                self.lastPointOfBase[1] = self.a[1] + (self.c[1] - self.a[1]) + (self.b[1] - self.a[1])
                self.lastPointOfBase[1] = self.a[2] + (self.c[2] - self.a[2]) + (self.b[2] - self.a[2])
            elif(self.rightAngle == "b"):
                self.lastPointOfBase[0] = self.b[0] + (self.c[0] - self.b[0]) + (self.a[0] - self.b[0])
                self.lastPointOfBase[1] = self.b[1] + (self.c[1] - self.b[1]) + (self.a[1] - self.b[1])
                self.lastPointOfBase[1] = self.b[2] + (self.c[2] - self.b[2]) + (self.a[2] - self.b[2])
            elif(self.rightAngle == "c"):
                self.lastPointOfBase[0] = self.c[0] + (self.b[0] - self.c[0]) + (self.a[0] - self.c[0])
                self.lastPointOfBase[1] = self.c[1] + (self.b[1] - self.c[1]) + (self.a[1] - self.c[1])
                self.lastPointOfBase[1] = self.c[2] + (self.b[2] - self.c[2]) + (self.a[2] - self.c[2])
        
    def checkIfSidesAreEqual(self):
        if(self.pointNotInPlane == "none"):
            print("ERROR - All points cannot be in same plane.")
            return False
        if(self.pointNotInPlane == "a"):
            if(self.bSide == self.dSide or self.bSide == self.cSide or self.cSide == self.dSide):
                return True
            else:
                return False
        elif(self.pointNotInPlane == "b"):
            if(self.aSide == self.dSide or self.aSide == self.cSide or self.cSide == self.dSide):
                return True
            else:
                return False
        elif(self.pointNotInPlane == "c"):
            if(self.aSide == self.dSide or self.aSide == self.bSide or self.bSide == self.dSide):
                return True
            else:
                return False
        else:
            if(self.aSide == self.bSide or self.aSide == self.cSide or self.bSide == self.cSide):
                return True
            else:
                return False

    def calculateSpaceDiagonal(self):
        if(self.pointNotInPlane == "a"):
            height1 = calculateHypotenusis3D(self.b[0], self.a[0], self.b[1], self.a[1], self.b[2], self.a[2])
            height2 = calculateHypotenusis3D(self.c[0], self.a[0], self.c[1], self.a[1], self.c[2], self.a[2])
            height3 = calculateHypotenusis3D(self.d[0], self.a[0], self.d[1], self.a[1], self.d[2], self.a[2])
            height4 = calculateHypotenusis3D(self.lastPointOfBase[0], self.a[0], self.lastPointOfBase[1], self.a[1], self.lastPointOfBase[2], self.a[2])

            print(f'Space diagonal: {max(height1, height2, height3, height4)}')
            return
        if(self.pointNotInPlane == "b"):
            height1 = calculateHypotenusis3D(self.b[0], self.a[0], self.b[1], self.a[1], self.b[2], self.a[2])
            height2 = calculateHypotenusis3D(self.c[0], self.b[0], self.c[1], self.b[1], self.c[2], self.b[2])
            height3 = calculateHypotenusis3D(self.d[0], self.b[0], self.d[1], self.b[1], self.d[2], self.b[2])
            height4 = calculateHypotenusis3D(self.lastPointOfBase[0], self.b[0], self.lastPointOfBase[1], self.b[1], self.lastPointOfBase[2], self.b[2])

            print(f'Space diagonal: {max(height1, height2, height3, height4)}')
            return
        if(self.pointNotInPlane == "c"):
            height1 = calculateHypotenusis3D(self.b[0], self.c[0], self.b[1], self.c[1], self.b[2], self.c[2])
            height2 = calculateHypotenusis3D(self.c[0], self.a[0], self.c[1], self.a[1], self.c[2], self.a[2])
            height3 = calculateHypotenusis3D(self.d[0], self.c[0], self.d[1], self.c[1], self.d[2], self.c[2])
            height4 = calculateHypotenusis3D(self.lastPointOfBase[0], self.c[0], self.lastPointOfBase[1], self.c[1], self.lastPointOfBase[2], self.c[2])

            print(f'Space diagonal: {max(height1, height2, height3, height4)}')
            return
        if(self.pointNotInPlane == "d"):
            height1 = calculateHypotenusis3D(self.b[0], self.d[0], self.b[1], self.d[1], self.b[2], self.d[2])
            height2 = calculateHypotenusis3D(self.c[0], self.d[0], self.c[1], self.d[1], self.c[2], self.d[2])
            height3 = calculateHypotenusis3D(self.d[0], self.a[0], self.d[1], self.a[1], self.d[2], self.a[2])
            height4 = calculateHypotenusis3D(self.lastPointOfBase[0], self.d[0], self.lastPointOfBase[1], self.d[1], self.lastPointOfBase[2], self.d[2])

            print(f'Space diagonal: {max(height1, height2, height3, height4)}')
            return