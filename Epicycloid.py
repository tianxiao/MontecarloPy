import math

def transformationF(x0,y0,theata, R):
	X = math.cos(theata)*x0 - math.sin(theata)*y0 - theata*R
	Y = math.sin(theata)*x0 - math.cos(theata)*y0 + R
	return X,Y
	

def drawParameters(filename, r):
	
	fout = open(filename,'w')

	theatS = -3*math.pi
	theatE = 3*math.pi
	n = 100
	deltatheat = (theatE-theatS)/n

	theata = theatS

	R = 1;

	for i in range(n):
		xypair = transformationF(0,-R*r,theata,R)
		fout.write("%f    %f\n"  %(xypair[0], xypair[1]))
		theata = theata + deltatheat

	fout.close

drawParameters('1.5r.txt',1.5)
drawParameters('1.0r.txt',1.0)
drawParameters('0.7r.txt',0.7)