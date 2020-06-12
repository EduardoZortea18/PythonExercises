import math

opositeSide = float(input('Oposite side: '))
adjacentSide = float(input('Adjacent side: '))

hypotenuse = math.hypot(opositeSide, adjacentSide)
print('The hypotenuse is {:.2f}'.format(hypotenuse))
