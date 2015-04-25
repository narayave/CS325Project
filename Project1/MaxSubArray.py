import os
import math
import sys
import string
import time
import csv

def PrintResults(sum, original, subarray):
	print "Original Array: " + str(original)
	print "Subarray:       " + str(subarray)
	print "Max Sum:        " + str(sum)

def Alg1(testArray):
	print 'Algorithm 1:'
	max = testArray[0]
	start = 0
	end = 0

	for i in range(0, len(testArray)):
		for j in range(i,len(testArray)):
			sum = 0
			for x in range(i,j+1):
				sum = sum + testArray[x]
			if sum > max:
				start = i
				end = j+1
				max = sum

	PrintResults(max, testArray, testArray[start:end])
	return max


def Alg2(testArray):
	print '\nAlgorithm 2:'
	max = 0
	start = 0
	end = 0
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

def Alg3(testArray):
	print '\nAlgorithm 3:'
	length = len(testArray)
	p = testArray[0:-(length/2)]	# Essentially sets p to be the set from 0 to middle of testArray.
	s = testArray[(length/2):length]	# Sets s to the second half of the testArray.
	first = Alg3(p)
	last = Alg3(s)
	pre = Alg3Helper(p)
	suf = Alg3Helper(s)
	center = pre + sub
	return
	# return array of max of concatenated arrays (pre + sub + center)

def Alg3HelperFunct(testArray):
	max = testArray[0]
	sum = 0
	for i in range(0,len(testArray)):
		sum = sum + testArray[i]
		print 'Sum = ' + str(sum) + ', Max = ' + str(max)
		if sum > max:
			max = sum
	print 'Max is ' + str(max) + '\n'
	return max


def Alg4(testArray):
	print '\nAlgorithm 4:'

	maybeStart = 0
	start = 0
	end = 0
	i = testArray[0]
	sum = testArray[0]
	small = Alg4Helper(0,i)

	for j in range(1,len(testArray)):
		i = i + testArray[j]
		if (i - small) > sum:
			start = maybeStart
			end = j+1
			sum = (i - small)
		if i < small:
			maybeStart = j+1
			small = i

	PrintResults(sum, testArray, testArray[start:end])
	return sum


def Alg4Helper(i,j):
	if (i < j):
		return i
	else:
		return j


if __name__ == '__main__':

	#print len(sys.argv)
	if len(sys.argv) < 2:
		print 'I need a text file along with this running this program.'
		print 'Playa, I\'m exiting now.\n'
		sys.exit()


	# text file needs to be passed in when running python code
	with open(sys.argv[1]) as f:
		testArray = map(int,f.read().split(','))


	# Algorithm 1 Enumeration method
	Alg1(testArray)
	# Algorithm 2 Better Enumeration method
	Alg2(testArray)
	# Algorithm 3 Divide and Conquer
	#Alg3(testArray)
	# Algorithm 4 Linear-time
	Alg4(testArray)

	print 'Finally done.'
