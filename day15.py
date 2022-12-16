import re
import copy

# AdventOfCode 2022

DAY = '15'
TEST = 1

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

# get blocked parts
blocked = []
targetRow = 10 if TEST else 2000000
for ( sx, sy, bx, by) in sensors:
  dist = abs( sx - bx) + abs( sy - by)
  dy = abs( sy - targetRow)
  print( sx, sy, bx, by, dist, dy)
  if  dist >= dy:
    print( "   ", sy, dist, dy)
    blocked.append( ( sx - ( dist - dy) , sx + ( dist - dy) ))

#remove overlaps
newBlocked = ['dummy']
toDelete = []
changed = True
while changed:
  newBlocked = []
  toDelete = []
  changed = False
  for i in range( 0, len(blocked) - 1):
    (x1, x2) = blocked[i]
    for j in range( i + 1, len(blocked)):
      (x3, x4) = blocked[j]
      if x2 >= x3 and x4 >= x1:
        changed = True
        newBlocked.append( (min( x1, x3), max( x2, x4)))
        toDelete.append( ( x1, x2))
        toDelete.append( ( x3, x4))
      else:
        newBlocked.append( ( x1, x2))
        newBlocked.append( ( x3, x4))
  if changed:
    blocked = copy.deepcopy( list(set(newBlocked)))
    for d in toDelete:
      while d in blocked:
        blocked.remove( d)
print( blocked)      


# numBlocked = []
# for ( x0, x1) in blocked:
#   for x in range( x0, x1 + 1):
#     numBlocked.append( x)
# setBlocked = set(numBlocked)
# result = len(setBlocked)
# for ( bx, by) in beacons:
#   if by == targetRow and bx in setBlocked:
#     result -= 1

# print( blocked)
# print( result)