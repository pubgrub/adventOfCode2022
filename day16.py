# AdventOfCode 2022

import re

DAY = '16'
TEST = 1

#get input data
if TEST == 1:
  testStr = 'test'
elif TEST == 2:
  testStr = 'mytest'
else:
  testStr = ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

p = re.compile( '.*? (\w\w).*?=(\d+).*?valve[s]*(\W\w\w,*+)')
for l in lines:
    r = p.finditer(l)
    for s in r:
        print( s)
        for g in s.groups():
            print( g)