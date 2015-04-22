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

def Alg3():
	print 'This is algorithm 3\n'

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
	Alg3()
	# Algorithm 4 Linear-time
	Alg4()

	print 'Finally done.'