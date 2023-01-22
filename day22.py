# AdventOfCode 2022

import re
DAY = '22'
TEST = 1

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line[:-1])
file.close()

p1 = re.compile('(\s*)([\.#]+)')
p2 = re.compile('#')
for y in range(0, len(lines) - 2):
  l = lines[y]
  m = p1.search(l)
   
  print( m.groups())
#  print( )
#  print( lines[y])



print( lines[len(lines) - 1])