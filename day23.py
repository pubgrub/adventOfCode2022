# AdventOfCode 2022

DAY = '23'
TEST = 0


#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

posToCheck = [[(-1,-1),(0,-1),(1,-1)],
              [(-1,1), (0,1), (1,1)],
              [(-1,-1),(-1,0),(-1,1)],
              [(1,-1),(1,0),(1,1)]
              ]
checkOrder = [0,1,2,3]

def getMinMax(positions):
  xMin = 99999
  xMax = -99999
  yMin = 99999
  yMax = -99999
  for (x, y) in positions:
    xMin = min(xMin, x)
    xMax = max(xMax, x)
    yMin = min(yMin, y)
    yMax = max(yMax, y)
  return(xMin, xMax, yMin, yMax)

def getFreeInRect( positions):
  (xMin, xMax, yMin, yMax) = getMinMax(positions)
  return (xMax - xMin + 1) * ( yMax - yMin + 1) - len(positions)

positions = {}
for y,l in enumerate(lines):
  for x,c in enumerate(l):
    if c == '#':
      positions[(x, y)] = ''

anyElveHasMoved = True
r = 0
while anyElveHasMoved:
  r += 1
  newPositions = {}
  anyElveHasMoved = False
  for (x, y) in positions:
    hasNeighbors = False
    moveDir = -1
    for dir in checkOrder:
      collision = False
      for (dX, dY) in posToCheck[dir]:
        if (x + dX, y + dY) in positions:
          collision = True
          hasNeighbors = True
          break
      if collision == False: 
        if moveDir == -1:
          moveDir = dir
    if hasNeighbors and moveDir > -1:
      (dX, dY) = posToCheck[moveDir][1]
      newPos = (x + dX, y + dY) 
      if newPos in newPositions:
        newPositions.pop(newPos)
      else:
        newPositions[newPos] = (x, y)
        anyElveHasMoved = True
  for newPos in newPositions:
    oldPos = newPositions[newPos]
    positions.pop(oldPos)
    positions[newPos] = ''
  checkOrder.append(checkOrder.pop(0))
  if r == 10:
    task1Solution = getFreeInRect( positions)   

print( 'Result Task 1: ', task1Solution)
print( 'Result Task 2: ', r)