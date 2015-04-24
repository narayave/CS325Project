import os
import math
import sys
import string
import time
import csv

def Alg1():
	print 'This is algorithm 1\n'

def Alg2():
	print 'This is algorithm 2\n'

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

def Alg3Helper(testArray):	
	max = testArray[0]
	sum = 0
	for i in range(0,len(testArray)):
		sum = sum + testArray[i]
		print 'Sum = ' + str(sum) + ', Max = ' + str(max)
		if sum > max:
			max = sum
	print 'Max is ' + str(max) + '\n'
	return max

def Alg4():
	print 'This is algorithm 4\n'


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
	Alg1()
	# Algorithm 2 Better Enumeration method
	Alg2()
	# Algorithm 3 Divide and Conquer
	Alg3(testArray)
	# Algorithm 4 Linear-time
	Alg4()

	print 'Finally done.'