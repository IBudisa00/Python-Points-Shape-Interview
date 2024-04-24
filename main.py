import shape
import utils

object = shape.Shape()
object.a, object.b, object.c, object.x = utils.getInfoFromFile()
utils.strToIntAllPoints(object)

typeOfShape = object.checkShapeType()
if(typeOfShape == "square"):
    print("Shape is square.")
    if(object.checkIfPointXInside()):
        print("X is inside square.")
    else:
        print("X isn't part of square.")
    print(f'Diagonal: {object.calculateDiagonal()}')
elif(typeOfShape == "rectangle"):
    print("Shape is rectangle.")
    if(object.checkIfPointXInside()):
        print("X is inside rectangle.")
    else:
        print("X isn't part of rectangle.")
    print(f'Diagonal: {object.calculateDiagonal()}')
else:
    print("Shape cannot be rectangle, exiting program...")