# AdventOfCode 2022

DAY = '12'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()

maxY = len(lines)
maxX = len(lines[0])

board = []
for y, l in enumerate(lines):
  for x, c in enumerate(list(l)):
    if c == 'S':
      start = y * maxX + x 
      lines[y] = lines[y].replace( 'S', 'a')
      c = 'a'
    if c == 'E':
      end = y * maxX + x
      lines[y] = lines[y].replace( 'E', 'z')
      c = 'z'
    board.append( ord(c ) - 97)

# print( board)

def getToCheck( p):
  ret = []
  x = p % maxX
  y = p // maxX
  if x < maxX - 1: ret.append( p + 1) 
  if x > 0: ret.append( p - 1) 
  if y < maxY - 1: ret.append( p + maxX)
  if y > 0: ret.append(  p - maxX)  
#  print( ret)
  return ret

# def solve( board, start, end):
#   toCheck = { start: True}
#   notVisited = maxY * maxX
#   minCost = [ notVisited] * len(board)
#   minCost[start] = 0

#   while len(toCheck):
#     ( sourcePos, dummy) = toCheck.popitem()
#     for checkPos in getToCheck( sourcePos):
#       if board[ checkPos] - board[ sourcePos] < 2:  # is reachable
#         if minCost[ checkPos] > minCost[sourcePos] + 1: # new best cost
#           minCost[ checkPos] = minCost[ sourcePos] + 1
#           toCheck[checkPos] = True
#   return minCost[ end]

def solve( board, start, end):
  toCheck = { end: True}
  notVisited = maxY * maxX
  minCost = [ notVisited] * len(board)
  minCost[end] = 0

  # Task 1

  while len(toCheck):
    ( sourcePos, dummy) = toCheck.popitem()
    for checkPos in getToCheck( sourcePos):
      if board[ sourcePos] - board[ checkPos] < 2:  # is reachable
        if minCost[ checkPos] > minCost[sourcePos] + 1: # new best cost
          minCost[ checkPos] = minCost[ sourcePos] + 1
          toCheck[checkPos] = True
  
  # + Task 2
  
  shortestFromA = notVisited
  for i, p in enumerate(board):
    if p == 0:
      shortestFromA = min(shortestFromA, minCost[ i])
  return (minCost[ start], shortestFromA)

(res1, res2) =  solve( board, start, end)

print( 'Result 1: ', res1)
print( 'Result 2: ', res2)

