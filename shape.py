import math
from math import acos
from math import degrees
from math import sqrt

class Shape:
    def __init__(self):
        self.a = (0,0)
        self.b = (0,0)
        self.c = (0,0)
        self.x = (0,0)
        self.rightAngle = "none"

    def checkAngles(self):
        alfa = degrees(acos((self.b**2 + self.c**2 - self.a**2)/ 2 * self.b * self.c))
        if(alfa == 90):
            self.rightAngle = "a"
            return True
        else:
            beta = degrees(acos((self.a**2 + self.c**2 - self.b**2)/ 2 * self.a * self.c))
            if(beta == 90):
                self.rightAngle = "b"
                return True
            else:
                if(180 - alfa - beta == 90):
                    self.rightAngle = "c"
                    return True
                else:
                    return False

    def checkIfRectangle(self):
        if(self.checkAngles()):
            return True
        else:
            return False

    def checkIfPointXInside():
        pass

    def calculateDiagonal(self):
        # in task it wasn't defined if calculating diagonal occures regardless of type of shape
        # so I went with relisation of it only in case of rectangle, that is why else case here
        # is for last angle (gamma) -> self.rightAngle cannot be "none" in this function
        if(self.rightAngle == "a"):
            diagonal = sqrt((self.b[0] - self.c[0])**2 + (self.b[1] - self.c[1])**2)
        elif(self.rightAngle == "b"):
            diagonal = sqrt((self.a[0] - self.c[0])**2 + (self.a[1] - self.c[1])**2)
        else:
            diagonal = sqrt((self.a[0] - self.b[0])**2 + (self.a[1] - self.b[1])**2)
        return diagonal