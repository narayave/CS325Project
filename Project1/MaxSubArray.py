import os
import math
import sys
import string
import time
import csv

def Alg1(testArray):
	print 'This is algorithm 1\n'
	max = testArray[0]

	for i in range(0, len(testArray)):
		for j in range(i,len(testArray)):
			sum = 0
			for x in range(i,j):
				sum = sum + testArray[x]
			if sum > max:
				max = sum
	print max
	return max


def Alg2(testArray):
	print 'This is algorithm 2\n'
	max = 0
	for i in range(0,len(testArray)):
		sum = 0
		for j in range(i,len(testArray)):
			sum = sum + testArray[j]
			if sum > max:
				max = sum
	print max
	return max

def Alg3(testArray):
	print 'This is algorithm 3'
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
	S = [len(testArray)]
	T = [len(testArray)]
	S[0] = testArray[0]
	T[0] = 0
	max = S[0]
	max_start = 0
	max_end = 0
	for i in range(1,len(testArray)):
		if (S[i - 1] > 0):
			S[i] = S[i-1] + testArray[i]
			T[i] = T[i-1]
		else:
			S[i] = A[i]
			T[i] = i

		if (S[i] > max):
			max_start = T[i]
			max_end = i
			max = S[i]

	print 'Max start '+ len(max_start)
	print 'Max end ' + len(max_end)

#def Alg4(testArray):
#	print 'This is algorithm 4\n'

#	i = testArray[0]
#	sum = testArray[0]
#	small = Alg4Helper(0,i)
	
#	for j in range(2,len(testArray)):
#		i = i + testArray[j]
#		if (i - small) > sum:
#			sum = (i - small)
#		if i < small:
#			small = i
	
#	print sum
#	return sum


#def Alg4Helper(i,j):
#	if (i < j):
#		return i
#	else:
#		return j


if __name__ == '__main__':

	#print len(sys.argv)
	if len(sys.argv) < 2:
		print 'I need a text file along with this running this program.'
		print 'Playa, I\'m exiting now.\n'
		sys.exit()
		

	# text file needs to be passed in when running python code
	with open(sys.argv[1]) as f:	
		testArray = map(int,f.read().split(','))
	
	print testArray		# Ints properly placed in list from file

	
	
	# Algorithm 1 Enumeration method
	Alg1(testArray)
	# Algorithm 2 Better Enumeration method
	Alg2(testArray)
	# Algorithm 3 Divide and Conquer
	#Alg3(testArray)
	# Algorithm 4 Linear-time
	Alg4(testArray)

	print 'Finally done.'