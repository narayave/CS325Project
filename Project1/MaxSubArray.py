import os
import math
import sys
import string
import time
import csv
import random

def randomNumGen(max):
	f = open('MSS_Problems.txt','a+')
	list = []
	for i in range(0,max):
		num = random.randint(-100,100)
		list.append(num)

	f.write(str(list) + '\n')
	f.close()

def PrintResults(sum, original, subarray):

	f = open('MSS_Results.txt','a+')
	f.write("Original Array: " + str(original) + '\n')
	f.write("Subarray:       " + str(subarray) + '\n')
	f.write("Max Sum:        " + str(sum) + '\n\n')
	print "Original Array: " + str(original)
	print "Subarray:       " + str(subarray)
	print "Max Sum:        " + str(sum)

def Alg1(testArray):
	print 'Algorithm 1:'
	max = testArray[0]
	start = 0
	end = 1

	if(len(testArray) == 1):
		PrintResults(testArray[0],testArray,testArray)
		return testArray[0]

	for i in range(0, len(testArray)):
		for j in range(i,len(testArray)):
			sum = 0
			for x in range(i,j + 1):
				sum = sum + testArray[x]
			if sum > max:
				start = i
				end = j + 1
				max = sum

	PrintResults(max, testArray, testArray[start:end])
	return max


def Alg2(testArray):
	print '\nAlgorithm 2:'
	max = testArray[0]
	start = 0
	end = 1

	if(len(testArray) == 1):
		PrintResults(testArray[0],testArray,testArray)
		return testArray[0]

	for i in range(0,len(testArray)):
		sum = 0
		for j in range(i,len(testArray)):
			sum = sum + testArray[j]
			if sum > max:
				start = i
				end = j + 1
				max = sum

	PrintResults(max, testArray, testArray[start:end])
	return max


def Alg3(testArray, dude):
	length = len(testArray)

	if length > 1:
		left = testArray[:int(length / 2)]	# Essentially sets p to be the set from 0 to middle of testArray.
		right = testArray[int(length / 2):]	# Sets s to the second half of the testArray.
		first = Alg3(left, 0)
		last = Alg3(right, 0)
		left.reverse()
		center = Alg3Helper(left) + Alg3Helper(right)
	else:
		first = last = center = testArray[0]

	if dude == len(testArray):
		print '\nAlgorithm 3:'
		PrintResults(max([first, last, center]), testArray, [first, last, center])
		#print max([first, last, center])

	return max([first, last, center])

def Alg3Helper(testArray):
	max = testArray[0]
	sum = 0
	for i in range(0, len(testArray)):
		sum += testArray[i]
		#print 'Sum = ' + str(sum) + ', Max = ' + str(max)
		if sum > max:
			max = sum
	#print 'Max is ' + str(max) + '\n'
	return max


def Alg4(testArray):
	print '\nAlgorithm 4:'

	if(len(testArray) == 1):
		PrintResults(testArray[0],testArray,testArray)
		return testArray[0]

	maybeStart = 0
	start = 0
	end = 1
	i = testArray[0]
	sum = testArray[0]
	small = Alg4Helper(0,i)
	if small < 0:
		maybeStart = 1
		end = 2

	for j in range(1,len(testArray)):
		i = i + testArray[j]
		if (i - small) > sum:
			start = maybeStart
			end = j + 1
			sum = (i - small)
		if i < small:
			maybeStart = j + 1
			small = i

	PrintResults(sum, testArray, testArray[start:end])
	return sum


def Alg4Helper(i,j):
	if (i < j):
		return i
	else:
		return j


if __name__ == '__main__':

	randomNumGen(int(sys.argv[1])) # length of array needs to be passed in when running python code

	foo = open('MSS_Problems.txt', 'r')

	while 1:
		
		line = foo.readline()
		if (line):
			line = line.replace('[', '')
			line = line.replace(']', '')
			testArray = line.split(',')
			testArray = map(int, testArray)
			#foo.close()
			#with open('MSS_Problems.txt') as f:
			#	testArray = map(int,f.read().split(','))
			print testArray

			try:
				os.remove('MSS_Results.txt')
			except OSError:
				pass

			alg1Start = time.clock()
			Alg1(testArray) 	# Algorithm 1 Enumeration method
			alg1End = time.clock()
			time1 = alg1End - alg1Start

			alg2Start = time.clock()
			Alg2(testArray)		# Algorithm 2 Better Enumeration method
			alg2End = time.clock()
			time2 = alg2End - alg2Start


			alg3Start = time.clock()
			Alg3(testArray, len(testArray)) 	# Algorithm 3 Divide and Conquer
			alg3End = time.clock()
			time3 = alg3End - alg3Start


			alg4Start = time.clock()
			Alg4(testArray)		# Algorithm 4 Linear-time
			alg4End = time.clock()
			time4 = alg4End - alg4Start


			f = open('MSS_Results.txt', 'a+')
			f.write('\n\nTimes for n = ' + str(len(testArray)) + '\n')
			f.write('Algorithm 1: ' + str(time1) + '\n')
			f.write('Algorithm 2: ' + str(time2) + '\n')
			f.write('Algorithm 3: ' + str(time3) + '\n')
			f.write('Algorithm 4: ' + str(time4) + '\n\n\n')
		else:
			break
	
	f.close()

	print 'Finally done.'
