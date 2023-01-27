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

xStart = []
yStart = []
xLen = []
yLen = []
xWalls = {}
yWalls = {}

xMax = len(max(lines[:-2], key=len)) - 1
cols = ['' for _ in range(xMax + 1)] 

p1 = re.compile('(\s*)([\.#]+)')
p2 = re.compile('#')
p3 = re.compile('(\d+)([LR])')
for y, l in enumerate(lines[:-2]):
  for x,c in enumerate( list(l + ' ' * xMax)[:xMax + 1]):
    cols[x] = cols[x] + c 
  m1 = p1.match(l)
  xStart.append(len(m1.group(1)))
  xLen.append(len(m1.group(2)))
  m2 = p2.finditer(m1.group(2))
  if not y in xWalls:
    xWalls[y] = []
  for w in m2:
    xWalls[y].append( w.start() + xStart[y])    

for x, l in enumerate(cols):
  print('l: ', l)
  m1 = p1.match(l)
  yStart.append(len(m1.group(1)))
  yLen.append(len(m1.group(2)))
  m2 = p2.finditer(m1.group(2))
  if not x in yWalls:
    yWalls[x] = []
  for w in m2:
    yWalls[x].append( w.start() + yStart[x])    

m1 = p3.finditer(lines[-1])

for match in m1:
  print( match.groups())



l = [ 0,1,2,3,4]
for i in reversed(l):
  print( i)

exit()





print( cols)
print( xStart, xLen)
print( xWalls)
print( yStart, yLen)
print( yWalls)
exit()



