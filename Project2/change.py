import os
import math
import sys
import string
import time
import csv
import random


def PrintResults(slowArray, greedyArray, dpArray, currency, amount, time1, time2, time3):

	slowNum = slowArray.pop(-1)
	greedyNum = greedyArray.pop(-1)  #pulling the total off of the end
	dpNum = dpArray.pop(-1)
	
	f = open("Amountchange.txt","w")
	f.write("Original Array: " + str(currency) + "\n")
	f.write("Amount: " + str(amount) + "\n")
 	f.write("Slow Array:     " + str(slowArray) + "\n")
 	f.write(str(slowNum) + "\n")
	f.write("Greedy Array:   " + str(greedyArray) + "\n")
	f.write(str(greedyNum) + "\n")
 	f.write("DP Array:       " + str(dpArray) + "\n")
 	f.write(str(dpNum) + "\n")
	f.write("======= Times =======" + "\n")
 	f.write("Slow:   " + str(time1) + "\n")
	f.write("Greedy: " + str(time2) + "\n")
 	f.write("DP:     " + str(time3) + "\n")

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

### does not work, caught in forever loop ###
def changeslow(currency, amount):
	print 'Slowly working...'

	if (amount == 0): return 0

	tmpResult1 = []
	tmpResult2 = []

	for i in range(0,len(currency)):
		tmpResult2.append(0)
		tmpResult1.append(-1)
		if (currency[i] <= amount):
			tmpResult2[i] = changeslow(currency, amount - currency[i])
			tmpResult1[i] = tmpResult2[i] + 1
			print 'looping'

	finalResult = -1

	for i in range(0,len(currency)):
		if (tmpResult1[i] >= 0):
			if (finalResult == -1 or tmpResult1[i] < finalResult):
				finalResult = tmpResult1[i]

	return(finalResult)



### THIS WORKS ###
def changegreedy(currency, amount):
	print '\nGreedily working...'
	
	numArray = [0] * len(currency)
	total = 0
	for i in range(0,len(currency)):
		if(currency[i] <= amount):
			num = amount / currency[i]
			numArray[i] = numArray[i] + num
			total = total + num
			amount -= num * currency[i]
	
	numArray.append(total) #sending the total through on the end of the array
	print numArray
	return numArray


### does not work ###
def changedp(currency, amount):
	print '\nDynamically working...'

	table = [[0 for x in range(amount+1)] for x in range(amount+1)]
	table[0][0] = 1

	for i in range(0,amount + 1):
		for j in range(0,len(currency)):
			if ((i + currency[j]) <= amount):
				table[i + currency[j]][j] += table[i][j]
			table[i][j + 1] += table[i][j]

	print 'Finished changedp'
	return table[amount]

if __name__ == '__main__':

	currency = [20,10,5,1]
	amount = 20700

# 	try:
# 		foo = open(sys.argv[1], 'r')
# 	except:
# 		print "Please specify a file name"
# 		print "usage: python MaxSubArray.py <filename>"
# 		print "\nNote: format of file must be: "
# 		print "\n[a1, a2, a3, ..., an]"
# 		print "[b1, b2, b3, ..., bn]"
# 		print "..."
# 		print "[*1, *2, *3, ..., *n]"
# 		print "\n\nexiting..."
# 		sys.exit()
#
# 	try:
# 		os.remove('MSS_Results.txt')
# 	except OSError:
# 		pass
#
# 	while 1:
#
# 		line = foo.readline()
# 		if (line):
# 			line = line.replace('[', '')
# 			line = line.replace(']', '')
# 			currency = line.split(',') #read the array of currency denominations
# 			#amount = #read the amount that we need to make change for
# 			try:
# 				testArray = map(int, testArray)
# 			except ValueError:
# 				print "Invalid file format"
# 				print "\nNote: format of file must be: "
# 				print "\n[a1, a2, a3, ..., an]"
# 				print "[b1, b2, b3, ..., bn]"
# 				print "..."
# 				print "[*1, *2, *3, ..., *n]"
# 				print "\n\nexiting..."
# 				sys.exit()
#
#

	
	slowStart = time.clock()
	changeslow(currency, amount)
	slowEnd = time.clock()
	time1 = slowEnd - slowStart

	greedyStart = time.clock()
	greedyArray = changegreedy(currency, amount)
	greedyEnd = time.clock()
	time2 = greedyEnd - greedyStart

	dpStart = time.clock()
	changedp(currency, amount)
	dpEnd = time.clock()
	time3 = dpEnd - dpStart
	
	PrintResults (slowArray, greedyArray, dpArray, currency, amount, time1, time2, time3)

	print '*********** Finished ***********'
	print "Note: These results can be found in Amountchange.txt"
