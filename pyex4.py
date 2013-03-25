import math

def length( x1, y1, x2, y2 ):
	l = math.sqrt( ( pow(x2 - x1, 2) + pow(y2 - y1, 2) ) )
	return l

inputX1 = int(input('PLEASE INPUT FIRST POINT (X) : '))
inputY1 = int(input('PLEASE INPUT FIRST POINT (Y) : '))
inputX2 = int(input('PLEASE INPUT SECOND POINT (X) : '))
inputY2 = int(input('PLEASE INPUT SECOND POINT (Y) : '))

print length( inputX1, inputY1, inputX2, inputY2 )
