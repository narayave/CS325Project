import sys


def getNum(line):
	index = line.index(":")
	return line[index+1:-2]

inFile = open(sys.argv[1], "r")
outFile = open(sys.argv[2], "w")

DPTimes = []
DPTotals = []
GTimes = []
GTotals = []
Amounts = []
while 1:
	line = inFile.readline()
	if line:
		if "Amount   " in line:
			Amounts.append(getNum(line))
		elif "Greedy Total" in line:
			GTotals.append(getNum(line))
		elif "Greedy Time" in line:
			GTimes.append(getNum(line))
		elif "DP Total" in line:
			DPTotals.append(getNum(line))
		elif "DP Time" in line:
			DPTimes.append(getNum(line))
		else:
			pass

	else:
		break

outFile.write("Amount,GTime,GTotal,DPTime,DPTotal\n")

for i in range(0, len(Amounts)):
	outFile.write(Amounts[i] + ",")
	outFile.write(GTimes[i] + ",")
	outFile.write(GTotals[i] + ",")
	outFile.write(DPTimes[i] + ",")
	outFile.write(DPTotals[i])
	outFile.write("\n")

inFile.close()
outFile.close()
