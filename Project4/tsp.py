import sys
import os
import math
import time


# helper function to calculate the distance between city1 & city2
def getDistance(city1, city2):
	# tried this initially with pow - it works, but it's slower
	dist1 = (city1[0]-city2[0])**2
	dist2 = (city1[1]-city2[1])**2
	return int(round(math.sqrt(dist1 + dist2),0))

# find tour for starting city
def getTour(start, cities):
	# initialize everything, process start city
	notVisited = [city for city in cities]
	tour = []
	totalDistance = 0
	notVisited.remove(start)
	tour.append(start)
	currentCity = start

	# go while there are still cities to visit
	while notVisited != []:
		# find the closest city from the current of the unvisited
		closest = (0, sys.maxint)
		for city in notVisited:
			distance = getDistance(cities[currentCity], cities[city])
			if distance < closest[1]:
				closest = (city, distance)
		# handle the found closest city
		tour.append(closest[0])
		notVisited.remove(closest[0])
		currentCity = closest[0]
		totalDistance += closest[1]
	# finish the tour when the loop is finished
	totalDistance += getDistance(cities[start], cities[closest[0]])
	return (tour, totalDistance)


if __name__ == "__main__":
	inFile = sys.argv[1]	
	
	f = open(inFile, "r")
	cities = {}

	while 1:
		line = f.readline()
		if line:
			data = line.strip("\n\r").split()
			# adds each city's coordinates to a dictionary as {(x, y)}
			# the index of the dictionary correlates to the key of the city 
			#     that is the first number column in the text doc which is not added
			cities[int(data[0])] = (int(data[1]), int(data[2]))
		else:
			break

	f.close()

	tours = []
	timeStart = time.clock()
	
	for i in range(0, len(cities)):
		tours.append(getTour(i, cities))
		
	tours.sort(key=lambda tup: tup[1])
	bestTour = tours[0]
	
	timeEnd = time.clock()
	timeTotal = timeEnd - timeStart

	# need to comment these 2 print lines out when turning in
	print "Total time: " + str(timeTotal) + " seconds"
	print "Best path distance: " + str(bestTour[1]) + "\n"

	outFile = open(inFile + ".tour", "w")
	outFile.write(str(bestTour[1]) + "\n")
	for j in bestTour[0]:
		outFile.write(str(j) + "\n")
	outFile.close()

