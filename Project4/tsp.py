import sys
import os
import math
import time


# helper function to calculate the distance between city1 & city2
def getDistance(city1, city2):
	# tried this initially with pow - it works, but it's slower
	dist1 = (city1[0]-city2[0])**2
	dist2 = (city1[1]-city2[1])**2
	# dont use decimals
	return int(round(math.sqrt(dist1 + dist2),0))


def getCycle(start, cities):
	unvisitedCities = [city for city in cities]
	cycle = []
	totalDistance = 0
	unvisitedCities.remove(start)
	cycle.append(start)
	currentCity = start

	while len(unvisitedCities) > 0:
		# assumes no cities are farther than this big number
		closestCity = (0, 9999999999)
		for city in unvisitedCities:
			distance = getDistance(cities[currentCity], cities[city])
			if distance < closestCity[1]:
				closestCity = (city, distance)
		cycle.append(closestCity[0])
		unvisitedCities.remove(closestCity[0])
		currentCity = closestCity[0]
		totalDistance += closestCity[1]
	# go back to start
	totalDistance += getDistance(cities[start], cities[closestCity[0]])
	return (cycle, totalDistance)


def getBestCycleTuple(cities, tFlag, timeoutTime):
	timeStart = time.clock()
	cycle = []
	
	timeout = 0
	for i in range(0, len(cities)):
		if tFlag:
			timeIteration = time.clock()
		cycle.append(getCycle(i, cities))
		if tFlag:
			timeIteration = time.clock() - timeIteration
			if time.clock() - timeStart > timeoutTime:
				print "TIMEOUT! REMOVING LAST ITERATION (WENT OVER TIME)"
				cycle.pop()
				timeout = 1
				break
			if time.clock() + timeIteration > timeStart + timeoutTime:
				print "PREDICTED TIMEOUT!"
				timeout = 1
				break

	cycle.sort(key=lambda tup: tup[1])
	bestCycle = cycle[0]

	timeTotal = time.clock() - timeStart

	if timeout:
		if timeTotal > timeoutTime:
			timeTotal = timeoutTime

	return (timeTotal, bestCycle)




if __name__ == "__main__":
	inFile = sys.argv[1]	
	try:
		timeoutTime = int(sys.argv[2])
		tFlag = 1
		print "Running with timeout of: " + str(timeoutTime) + " seconds"
	except:
		timeoutTime = 0
		tFlag = 0
		print "Running with no timeout"

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

	result = getBestCycleTuple(cities, tFlag, timeoutTime);
	timeTotal = result[0]
	bestCycle = result[1] 

	# need to comment these 2 print lines out when turning in
	print "Total time: " + str(timeTotal) + " seconds"
	print "Best path distance: " + str(bestCycle[1]) + "\n"

	outFile = open(inFile + ".tour", "w")
	outFile.write(str(bestCycle[1]) + "\n")
	for j in bestCycle[0]:
		outFile.write(str(j) + "\n")
	outFile.close()

