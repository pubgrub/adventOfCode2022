# AdventOfCode 2022

import re
DAY = '22'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line[:-1])
file.close()


steps = [(1,0),(0,1),(-1,0),(0,-1)]

def getNewPos(pos, dir):
  return (pos[0] + steps[dir][0], pos[1] + steps[dir][1]  )

lines.insert(0,'')
pOrder = re.compile('(\d+)([LR])')
walkList = []
turnValue = {'L': -1, 'R':1}
l = lines.pop()
for match in  pOrder.finditer(l):
  walkList.append((int(match.group(1)), turnValue[match.group(2)])) 

xStart = [0]
yStart = [0]
xLen = [0]
yLen = [0]
xWalls = {}
yWalls = {}

xMax = len(max(lines, key=len)) + 1

for i in range(0,len(lines)):
  lines[i] = (' ' + lines[i] + ' ' * (xMax + 1))[:xMax + 1]

cols = ['' for _ in range(xMax + 1)] 
print( lines)


p1 = re.compile('(\s*)([\.#]+)')
p2 = re.compile('#')
for y, l in enumerate(lines):
  for x,c in enumerate(l):
    cols[x] = cols[x] + c 
  if y > 0 and y < len(lines) - 1:
    m1 = p1.match(l)
    xStart.append(len(m1.group(1)))
    xLen.append(len(m1.group(2)))
    m2 = p2.finditer(m1.group(2))
    if not y in xWalls:
      xWalls[y] = []
    for w in m2:
      xWalls[y].append( w.start() + xStart[y])    


for x, l in enumerate(cols[1:-1]):
  print('l: ', l)
  m1 = p1.match(l)
  yStart.append(len(m1.group(1)))
  yLen.append(len(m1.group(2)))
  m2 = p2.finditer(m1.group(2))
  if not x in yWalls:
    yWalls[x] = []
  for w in m2:
    yWalls[x].append( w.start() + yStart[x])    



dir = 0

pos = (xStart[1],1)
print('pos: ',pos)
for (dist,turn) in walkList:
  wrap = False
  while dist:
    if wrap:
      newPos = getNewPos(newPos,dir)
      wrap = False
    else:
      newPos = getNewPos(pos,dir)
    symbol = lines[newPos[1]][newPos[0]]     
    if symbol == '.':
      pos = newPos
      print( 'pos: ', pos)
      dist -= 1
    elif symbol == '#':
      dist = 0
    elif symbol == ' ':
      wrap = True
      if dir == 0:
        newPos = (xStart[pos[1]] - 1,pos[1])
      elif dir == 1:
        newPos = (pos[0],yStart[pos[0]] - 1)
      elif dir == 2:
        newPos = (xStart[pos[1]] + xLen[pos[1]],pos[1])
      elif dir == 3:
        newPos = (pos[0],yStart[pos[0]] + yLen[pos[0]])
  dir = (dir + turn) % 4






print( cols)
print( xStart, xLen)
print( xWalls)
print( yStart, yLen)
print( yWalls)
print( pos, dir)
print( pos[0] * 4 + pos[1] * 1000 + dir)




