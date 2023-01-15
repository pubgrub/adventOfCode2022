import copy
# AdventOfCode 2022

DAY = '24'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

print( len(lines), len(lines[0]))



print( -5 % 4)