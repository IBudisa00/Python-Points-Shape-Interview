import shape
import utils

kocka = shape.Shape()
kocka.a, kocka.b, kocka.c, kocka.x = utils.getInfoFromFile()
utils.strToIntAllPoints(kocka)

if(kocka.checkIfRectangle()):
    print("Shape is rectangle.")
    if(kocka.checkIfPointXInside()):
        print("X is inside rectangle.")
    else:
        print("X isn't part of rectangle.")
    print(f'Diagonal: {kocka.calculateDiagonal()}')
else:
    print("Shape cannot be rectangle, exiting program...")