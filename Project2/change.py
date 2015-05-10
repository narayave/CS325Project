import os
import math
import sys
import string
import time
import csv
import random


def PrintResults(resultFile, slowArray, greedyArray, dpArray, currency, amount, time1, time2, time3):

	slowNum = slowArray.pop(-1)
	greedyNum = greedyArray.pop(-1)  #pulling the total off of the end
	dpNum = dpArray.pop(-1)

	resultFile.write("Slow Array:   " + str(slowArray) + "\n")
	resultFile.write("Slow Total:   " + str(slowNum) + "\n")
	resultFile.write("Slow Time:    " + str(time1) + "\n")
	resultFile.write("Greedy Array: " + str(greedyArray) + "\n")
	resultFile.write("Greedy Total: " + str(greedyNum) + "\n")
	resultFile.write("Greedy Time:  " + str(time2) + "\n")
	resultFile.write("DP Array:     " + str(dpArray) + "\n")
	resultFile.write("DP Total:     " + str(dpNum) + "\n")
	resultFile.write("DP Time:      " + str(time3) + "\n\n")

	print "Currency Array: " + str(currency)
	print "Amount:         " + str(amount)
	print "Slow Array:     " + str(slowArray)
	print "Slow Total:     " + str(slowNum)
	print "Greedy Array:   " + str(greedyArray)
	print "Greedy Total:   " + str(greedyNum)
	print "DP Array:       " + str(dpArray)
	print "DP Total:       " + str(dpNum)
	print "======= Times =======\n"
	print "Slow:   " + str(time1) + "\n"
	print "Greedy time: " + str(time2) + "\n"
	print "DP:     " + str(time3) + "\n\n\n"


def changeslowhelper(currency, amount):
	if amount == 0:
		return []
	for coin in currency:
		if coin == amount:
			return [coin]
	minCoins = -1
	coins = []
	for i in range(1, amount/2 + 1):
		temp = []
		temp.extend(changeslowhelper(currency, i))
		temp.extend(changeslowhelper(currency, amount - i))
		numCoins = len(temp)

		if minCoins == -1:
			minCoins = numCoins
			coins = temp
		elif numCoins < minCoins:
			minCoins = numCoins
			coins = temp


	return coins


def changeslow(currency, amount):
	coins = changeslowhelper(currency, amount)

	result = []
	for coin in currency:
		result.append(coins.count(coin))

	result.append(len(coins))

	return result




def changegreedy(currency, amount):
	numArray = [0] * len(currency)
	total = 0
	for i in range(len(currency)-1,-1,-1):
		if(currency[i] <= amount):
			num = amount / currency[i]
			numArray[i] = numArray[i] + num
			total = total + num
			amount -= num * currency[i]

	numArray.append(total) #sending the total through on the end of the array
	return numArray


def changedp(currency,amount):
	minArray = [0]
	firstCoinArray = [0]
	coin = 0

	for j in range(1, amount+1):
		min = -1
		for i in range(0, len(currency)):
			if currency[i] <= j:
				if min == -1:
					min = 1 + minArray[j - currency[i]]
					coin = i
				elif 1 + minArray[j - currency[i]] < min:
					min = 1 + minArray[j - currency[i]]
					coin = i
		#C[p] = min
		minArray.append(min)
		#S[p] = coin
		firstCoinArray.append(coin)

	coins = []
	while amount > 0:
		coins.append(currency[firstCoinArray[amount]])
		amount = amount - currency[firstCoinArray[amount]]

	numCoins = len(coins)

	result = []
	for coin in currency:
		result.append(coins.count(coin))

	result.append(numCoins)

	return result


def getResultFileName(name):
	return name[:-4] + "change.txt"

if __name__ == '__main__':
	currencies = []
	ammounts = []

	inFile = open(sys.argv[1], "r")
	while 1:
		line = inFile.readline()
		if line:
			line = line.replace('[', '')
			line = line.replace(']', '')
			tempArray = line.split(',')
			temp2 = []
			for x in tempArray:
				temp2.append(int(x))

			currencies.append(temp2)

			line = inFile.readline()
			ammounts.append(int(line))
		else:
			break

	inFile.close()

	resultFileName = getResultFileName(sys.argv[1])
	resultFile = open(resultFileName, "w")


	for i in range(0, len(currencies)):
		currency = sorted(currencies[i])
		amount = ammounts[i]

		if amount < 32:
			print "slow..."
			slowStart = time.clock()
			slowArray = changeslow(currency, amount)
			slowEnd = time.clock()
			time1 = slowEnd - slowStart
		else:
			print "Not running changeslow, amount too large. Must be less than 32"
			slowArray = ["NOT RUN - Amount must be less than 32", "NOT RUN - Amount must be less than 32"]
			time1 = "NOT RUN - Amount must be less than 32"

		print "greedy..."
		greedyStart = time.clock()
		greedyArray = changegreedy(currency, amount)
		greedyEnd = time.clock()
		time2 = greedyEnd - greedyStart

		print "DP..."
		dpStart = time.clock()
		dpArray = changedp(currency, amount)
		dpEnd = time.clock()
		time3 = dpEnd - dpStart

		print "\n\n"
		PrintResults (resultFile, slowArray, greedyArray, dpArray, currency, amount, time1, time2, time3)

	print '*********** Finished ***********'
	print "Note: These results can be found in " + resultFileName

	resultFile.close()
