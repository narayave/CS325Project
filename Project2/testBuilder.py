import sys

filename = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
increment = int(sys.argv[4])
array = sys.argv[5]

f = open(filename, "w")

for i in range(start, end+1, increment):
	f.write(array + "\n")
	f.write(str(i) + "\n")
