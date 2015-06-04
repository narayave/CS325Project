import sys
import os
import math
import time


# calculate the distance between city1 & city2 using the pythagorean theorem
def getDistance(city1, city2):
	dist1 = (city1[0]-city2[0])**2
	dist2 = (city1[1]-city2[1])**2
	distance = int(round(math.sqrt(dist1 + dist2),0))
	return distance

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
		closest = (0, float("inf")) # big number, has to be a tuple
		# find the closest city from the current of the unvisited
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
			# add city to dictionary as {city: (x, y)}
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

	print "Total time: " + str(timeTotal) + " seconds"
	print "Best path distance: " + str(bestTour[1]) + "\n"

	outFile = open(inFile + ".tour", "w")
	outFile.write(str(bestTour[1]) + "\n")

	for city in bestTour[0]:
		outFile.write(str(city) + "\n")
	outFile.close()

