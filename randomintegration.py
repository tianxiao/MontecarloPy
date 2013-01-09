import random

def checkValueFun(randomX, randomY, fun):
	if randomY < fun(randomX):
		return True
	else:
		return False
	
	
def integradeFun(x):
	return x*x + 1.0

totalSample = 1000000
inM = 0 
outN = 0

for i in range(totalSample):
	if checkValueFun(random.random(),2*random.random(),integradeFun):
		inM = inM +1
	else:
		outN = outN +1
		

print inM ,outN
print inM*1.0/totalSample * 2
	
	