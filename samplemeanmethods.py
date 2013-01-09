import random
import math

def integradeFun(x):
	return math.e**x

# sample times
totalSample = 1000

leftrange = 0.0
rightrange = 3.0

sum = 0.0


for i in range(totalSample):
	sum = sum + integradeFun(random.uniform(leftrange,rightrange))
	
	
print "Integration results:"
print (rightrange-leftrange)*sum/totalSample


	