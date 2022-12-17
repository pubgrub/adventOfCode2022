import copy

# AdventOfCode 2022

DAY = '14'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()

ROCK = 1
SAND = 2

# make cave
occ_orig = {}
maxY = 0
for l in lines:
  coordList = [ int(i) for i in l.replace( ' -> ', ',').split(',')]
  for i in range( 0, len(coordList) - 2, 2):
    (startX, startY) = coordList[i], coordList[i+1]
    if i < len( coordList) - 1:
      ( endX, endY) = coordList[ i+2], coordList[ i+3]
    if startX == endX:
      dir = 1 if startY < endY else -1
      for y in range( startY, endY + dir, dir):
        occ_orig[( startX, y) ] = ROCK
    else:
      dir = 1 if startX < endX else -1
      for x in range( startX, endX + dir, dir):
        occ_orig[( x, startY) ] = ROCK
    maxY  = max( maxY, startY, endY)    
floor = maxY + 2

def solve( task):
  occ = copy.deepcopy( occ_orig)
  numSand = 0
  done = False
  while not done:
    x = 500
    y = 0
    finalPos = False
    while not finalPos:
      if not (x, y+1) in occ:
        y += 1
      elif not (x-1, y+1) in occ:
        y += 1
        x -= 1
      elif not ( x+1, y+1) in occ:
        y += 1
        x += 1
      else:
        finalPos = True
        numSand += 1
        occ[ (x, y)] = SAND 
        if x == 500 and y == 0:
          done = True
      if task == 1 and y == maxY:
        finalPos = True
        done = True
      if task == 2 and y == floor -1:
        occ[ ( x, floor)] = ROCK 
        occ[ ( x+1, floor)] = ROCK 
        occ[ ( x-1, floor)] = ROCK 
       
  return numSand

print( ' Result Task 1: ', solve(1))       
print( ' Result Task 2: ', solve(2))       
