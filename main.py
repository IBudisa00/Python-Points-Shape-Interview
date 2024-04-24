import shape
import utils

#regarding number of lines correct shape class will be used (2D or 3D) --> (4 lines or 5 lines) 
numberOfLinesInFile = utils.getNumberOfLinesFromFile()
if(numberOfLinesInFile == 4):
    object = shape.Shape2D()
elif(numberOfLinesInFile == 5):
    object = shape.Shape3D()
else:
    print("ERROR - Incorrect number of lines (arguments) in file.")

if(isinstance(object,shape.Shape2D)):
    utils.strToIntAllPoints2D(object)
    typeOfShape = object.checkShapeType()

elif(isinstance(object,shape.Shape3D)):
    utils.strToIntAllPoints3D(object)
    object.checkShapeType()