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

def PrintResults(sum1, sum2, sum3, sum4, original, subarray, time1, time2, time3, time4):
	f = open('MSS_Results.txt','a+')
	f.write("Original Array: " + str(original) + "\n")
	f.write("Subarray:       " + str(subarray) + "\n")
	f.write("Sum for alg1:   " + str(sum1) + "\n")
	f.write("Sum for alg2:   " + str(sum2) + "\n")
	f.write("Sum for alg3:   " + str(sum3) + "\n")
	f.write("Sum for alg4:   " + str(sum4) + "\n\n")
	f.write('Times for n = ' + str(len(testArray)) + '\n')
	f.write('Alg1: ' + str(time1) + '\n')
	f.write('Alg2: ' + str(time2) + '\n')
	f.write('Alg3: ' + str(time3) + '\n')
	f.write('Alg4: ' + str(time4) + '\n\n\n')

	print "Original Array: " + str(original)
	print "Subarray:       " + str(subarray)
	print "Sum for alg1:   " + str(sum1)
	print "Sum for alg2:   " + str(sum2)
	print "Sum for alg3:   " + str(sum3)
	print "Sum for alg4:   " + str(sum4) + "\n"
	print 'Times for n = ' + str(len(testArray)) + '\n'
	print 'Alg1: ' + str(time1) + '\n'
	print 'Alg2: ' + str(time2) + '\n'
	print 'Alg3: ' + str(time3) + '\n'
	print 'Alg4: ' + str(time4) + '\n\n\n'




def Alg1(testArray):
	print 'Working on Alg1...'
	max = testArray[0]
	start = 0
	end = 1

	for i in range(0, len(testArray)):
		for j in range(i,len(testArray)):
			sum = 0
			for x in range(i,j + 1):
				sum = sum + testArray[x]
			if sum > max:
				start = i
				end = j + 1
				max = sum

	if(max >= 0):
		return [max, testArray[start:end]]
	else:
		return [0, []]



def Alg2(testArray):
	print '\nWorking on Alg2...'
	maxSum = testArray[0]
	start = 0
	end = 1

	for i in range(0,len(testArray)):
		sum = 0
		for j in range(i,len(testArray)):
			sum = sum + testArray[j]
			if sum > maxSum:
				start = i
				end = j + 1
				maxSum = sum

	return max(maxSum,0)


def Alg3(testArray, initStartLen):
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

	if initStartLen == length:
		print '\nWorking on Alg3...'
		return max(max([first, last, center]), 0)

	return max([first, last, center])

def Alg3Helper(testArray):
	max = testArray[0]
	sum = 0
	for i in range(0, len(testArray)):
		sum += testArray[i]
		if sum > max:
			max = sum
	return max


def Alg4(testArray):
	print '\nWorking on Alg4...'

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

	return max(sum, 0)


def Alg4Helper(i,j):
	if (i < j):
		return i
	else:
		return j


if __name__ == '__main__':

	try:
		foo = open(sys.argv[1], 'r')
	except:
		print "Please specify a file name"
		print "usage: python MaxSubArray.py <filename>"
		print "\nNote: format of file must be: "
		print "\n[a1, a2, a3, ..., an]"
		print "[b1, b2, b3, ..., bn]"
		print "..."
		print "[*1, *2, *3, ..., *n]"
		print "\n\nexiting..."
		sys.exit()

	try:
		os.remove('MSS_Results.txt')
	except OSError:
		pass

	while 1:

		line = foo.readline()
		if (line):
			line = line.replace('[', '')
			line = line.replace(']', '')
			testArray = line.split(',')
			try:
				testArray = map(int, testArray)
			except ValueError:
				print "Invalid file format"
				print "\nNote: format of file must be: "
				print "\n[a1, a2, a3, ..., an]"
				print "[b1, b2, b3, ..., bn]"
				print "..."
				print "[*1, *2, *3, ..., *n]"
				print "\n\nexiting..."
				sys.exit()



			alg1Start = time.clock()
			sum1 = Alg1(testArray) 	# Algorithm 1 Enumeration method
			alg1End = time.clock()
			time1 = alg1End - alg1Start

			alg2Start = time.clock()
			sum2 = Alg2(testArray)		# Algorithm 2 Better Enumeration method
			alg2End = time.clock()
			time2 = alg2End - alg2Start


			alg3Start = time.clock()
			sum3 = Alg3(testArray, len(testArray)) 	# Algorithm 3 Divide and Conquer
			alg3End = time.clock()
			time3 = alg3End - alg3Start


			alg4Start = time.clock()
			sum4 = Alg4(testArray)		# Algorithm 4 Linear-time
			alg4End = time.clock()
			time4 = alg4End - alg4Start

			PrintResults(sum1[0], sum2, sum3, sum4, testArray, sum1[1], time1, time2, time3, time4)

		else:
			break

	foo.close()

	print 'Finally done.'
	print "Note: These results can be found in MSS_Results.txt"
