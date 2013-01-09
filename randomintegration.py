import random

def checkValueFun(randomX, randomY, fun):
	if randomY < fun(randomX):
		return True
	else:
		return False
	
	
def integradeFun(x):
	return x*x + 1.0

# total sample number
totalSample = 1000000
# point in the integration area
inM = 0 
# point out of the integration area
outN = 0

for i in range(totalSample):
	if checkValueFun(random.random(),2*random.random(),integradeFun):
		inM = inM +1

		

print inM ,outN
# 2 is hard code is the total trial area
# the 1*2 rectangle region
print inM*1.0/totalSample * 2
	
	