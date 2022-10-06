# in a 1 x 1 sqaure, randomly choose two points
# what is the average distance between the two

import random
import math

#select a random point
def pointselector():
	return round(random.random(),4)

	
#run the montecarlo
def runmontecarlo(numtrials):
	points = []
	for i in range(numtrials):
		distance = 0.0000
		for j in range(2):
			x = pointselector()
			y = pointselector()
			point = (x,y)
			#print(point)
			points.extend(tuple(point))
			#print(points)
		distance += math.dist([points[0],points[1]],[points[2],points[3]])
	return distance/numtrials

#print the result
print(runmontecarlo(10))
print(runmontecarlo(1000))
print(runmontecarlo(10000))
print(runmontecarlo(100000))






