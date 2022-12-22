import re
import copy

# AdventOfCode 2022

DAY = '15'
TEST = 1

# for Task 1, data not in input file
targetRow = 10 if TEST else 2000000
# for Task 2, data not in input file
minBox = 0 
maxBox = 20 if TEST else 4000000

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()

pattern = re.compile( r".*?x=([-]*\d+).*?y=([-]*\d+).*?x=([-]*\d+).*?y=([-]*\d+)")

# get sensors and beacons from input
sensors = []
beacons = []
for l in lines:
  x = re.match( pattern, l )
  ( sx, sy, bx, by) = x.groups()
  sensors.append( ( int(sx), int(sy), int(bx), int(by)))
  beacons.append( ( int(bx), int(by)))
beacons = list(set( beacons))

blockedRows = {}

# get blocked parts
def fillBlockedTask_1():
  global blockedRows 
  blockedRows = {}
  for ( sx, sy, bx, by) in sensors:
    print( sy, sy, bx, by)
    dist = abs( sx - bx) + abs( sy - by)
    for y in range( sy - dist, sy + dist + 1):
      dy = abs( y - sy)
      minBlocked = sx - ( dist - dy)
      maxBlocked = sx + ( dist - dy)
      if not y in blockedRows:
        blockedRows[y] = []
      if by == y:
        if bx == minBlocked:
          minBlocked += 1
        else:
          maxBlocked -= 1
      if minBlocked <= maxBlocked:
        blockedRows[y].append( (minBlocked, maxBlocked))

# get blocked parts
def fillBlockedTask_2():
  blockedRows = {}
  for ( sx, sy, bx, by) in sensors:
    print( sy, sy, bx, by)
    dist = abs( sx - bx) + abs( sy - by)
    for y in range( max(minBox, sy - dist), min( sy + dist + 1, maxBox)):
      dy = abs( y - sy)
      minBlocked = max( minBox, sx - ( dist - dy))
      maxBlocked = min( sx + ( dist - dy), maxBox)
      if not y in blockedRows:
        blockedRows[y] = []
      if by == y:
        if bx == minBlocked:
          minBlocked += 1
        else:
          maxBlocked -= 1
      if minBlocked <= maxBlocked:
        blockedRows[y].append( (minBlocked, maxBlocked))
  print( beacons)
  for ( bx, by) in beacons:
    if by in blockedRows:
      blockedRows[by].append( ( bx, bx))
    else:
      blockedRows[by] = ( bx, bx)

#remove overlaps
def removeOverlaps():
  newBlocked = 0
  toDelete = []

  for y in blockedRows:
    if y % 10000 == 0:
      print( y)
    changed = True
    while changed:
      if newBlocked:
        blockedRows[y].remove( (x1, x2 ))
        blockedRows[y].remove( (x3, x4 ))
        blockedRows[y].append( newBlocked)
        newBlocked = 0 
      changed = False
      for i in range( 0, len(blockedRows[y]) - 1):
        (x1, x2) = blockedRows[y][i]
        for j in range( i + 1, len(blockedRows[y])):
          (x3, x4) = blockedRows[y][j]
          if x2 >= x3 - 1  and x4 >= x1 - 1:
            changed = True
            newBlocked = (min( x1, x3), max( x2, x4))
            break
        if changed:
          break

print( blockedRows)      

# Task 1

fillBlockedTask_1()
removeOverlaps()
blocked = 0
for ( r1, r2) in blockedRows[ targetRow]:
  blocked += r2 - r1 + 1
print( blocked)

# Task 2

fillBlockedTask_2()
removeOverlaps()
for y in range( minBox, maxBox + 1):
  print( y, blockedRows[y])

