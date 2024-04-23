import utils
from utils import calculateHypotenusis
import math
from math import acos
from math import degrees

class Shape:
    def __init__(self):
        self.a = (0,0)
        self.b = (0,0)
        self.c = (0,0)
        self.x = (0,0)
        self.rightAngle = "none"
        self.aSide = 0
        self.bSide = 0
        self.cSide = 0

    def calculateSides(self):
        self.aSide = calculateHypotenusis(self.b[0], self.b[1], self.c[0], self.c[1])
        self.bSide = calculateHypotenusis(self.a[0], self.a[1], self.c[0], self.c[1])
        self.cSide = calculateHypotenusis(self.a[0], self.a[1], self.b[0], self.b[1])

    def checkAngles(self):
        self.calculateSides()
        alfa = round(degrees(acos((self.bSide**2 + self.cSide**2 - self.aSide**2)/ (2 * self.bSide * self.cSide))), 3)
        if(alfa == 90.0):
            self.rightAngle = "a"
            return True
        else:
            beta = round(degrees(acos((self.aSide**2 + self.cSide**2 - self.bSide**2)/ (2 * self.aSide * self.cSide))),3)
            if(beta == 90.0):
                self.rightAngle = "b"
                return True
            else:
                if(180 - alfa - beta == 90.0):
                    self.rightAngle = "c"
                    return True
                else:
                    return False

    def checkIfRectangle(self):
        if(self.checkAngles()):
            return True
        else:
            return False

    def checkIfPointXInside(self):
        if(self.rightAngle == "a"):
            factor1 = (self.a[0] * (self.c[1] - self.a[1]) + (self.x[1] - self.a[1]) * (self.c[0] - self.a[0]) - (self.x[0] * (self.c[1] - self.a[1])))/((self.b[1] - self.a[1]) * (self.c[0] - self.a[0]) - ((self.b[0] - self.a[0]) * (self.c[1] - self.a[1])))
            factor2 = (self.x[1] - self.a[1] - (factor1 * (self.b[1] - self.a[1])))/(self.c[1] - self.a[1])
            factorSum = round(factor1 + factor2, 3)
            if(factor1 >= 0 and factor2 >= 0 and factorSum <= 2):
                return True
            else:
                return False
        elif(self.rightAngle == "b"):
            factor1 = (self.b[0]*(self.c[0] - self.b[0]) + (self.x[1] - self.b[1]) * (self.c[0] - self.b[0]) - (self.x[0] * (self.c[0] - self.b[0])))/((self.a[1] - self.b[1]) * (self.c[0] - self.b[0]) - ((self.a[0] - self.b[0]) * (self.c[0] - self.b[0])))
            factor2 = (self.x[1] - self.b[1] - (factor1 * (self.a[1] - self.b[1])))/(self.c[1] - self.b[1])
            factorSum = round(factor1 + factor2, 3)
            if(factor1 >= 0 and factor2 >= 0 and factorSum <= 2):
                return True
            else:
                return False
        else:
            factor1 = (self.c[0] * (self.b[1] - self.c[1]) + (self.x[1] - self.c[1]) * (self.b[0] - self.c[0]) - (self.x[0] * (self.b[1] - self.c[1])))/((self.a[1] - self.c[1]) * (self.b[0] - self.c[0]) - ((self.a[0]- self.c[0]) * (self.b[1] - self.c[1])))
            factor2 = (self.x[1] - self.c[1] - (factor1 * (self.a[1] - self.c[1])))/(self.b[1] - self.c[1])
            factorSum = round(factor1 + factor2, 3)
            if(factor1 >= 0 and factor2 >= 0 and factorSum <= 2):
                return True
            else:
                return False

    def calculateDiagonal(self):
        # in task it wasn't defined if calculating diagonal occures regardless of type of shape
        # so I went with relisation of it only in case of rectangle, that is why else case here
        # is for last angle (gamma) -> self.rightAngle cannot be "none" in this function
        if(self.rightAngle == "a"):
            diagonal = self.aSide
        elif(self.rightAngle == "b"):
            diagonal = self.bSide
        else:
            diagonal = self.cSide
        return diagonal
    