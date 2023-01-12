# AdventOfCode 2022

DAY = '18'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

def solve1():
  dubl = {}
  blocks = {}
  minCoord = [99999, 99999, 99999]
  maxCoord = [-1, -1, -1]
  offs = [[1,0,0], [0,1,0], [0,0,1]]
  for l in lines:
    c = [int(i) for i in l.split(',')]
    blocks[tuple(c)] = 'lava'
    for plane in range( 0,3):
      maxCoord[plane] = max( maxCoord[plane], c[plane])
      minCoord[plane] = min( minCoord[plane], c[plane])
      try:
        dubl[( plane, c[0], c[1], c[2])] += 1
      except KeyError:
        dubl[( plane, c[0], c[1], c[2])] = 0
      try:
        dubl[( plane, c[0] + offs[plane][0], c[1] + offs[plane][1], c[2] + offs[plane][2])] += 1
      except KeyError:
        dubl[( plane, c[0] + offs[plane][0], c[1] + offs[plane][1], c[2] + offs[plane][2])] = 0
  return dubl, blocks, maxCoord, minCoord

def outOfBounds( c):
  for i in range( 0, 3):
    if c[i] < minCoord[i] - 1 or c[i] > maxCoord[i] + 1:
      return True
  return False

neighborBlocks = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def fill( c):
  while blocksToCheck:
    c = blocksToCheck[0]
    if c in blocks:
      print( 'Block already known: ', c)
      blocks
    if outOfBounds( c):
      print( 'Out of Bounds: ', c)
      return
    blocks[ c] = 'water'
    offs = [(1,0,0), (0,1,0), (0,0,1)]
    for plane in range( 0, 3):
      #print ( tuple([plane]) + c )
      if tuple([plane]) + c in surfaces:
        surfaces[tuple([plane]) + c] = 1
      c1 = tuple( map(lambda i, j: i + j, c, offs[plane]))
      #print( c, plane, offs[plane], c1)
      if tuple([plane]) + c1 in surfaces:
        surfaces[tuple([plane]) + c1] = 1
        print( 'New surface: ', surfaces)

    for n in neighborBlocks:
      neighbor = tuple( map(lambda i, j: i + j, c, n))
      fill( neighbor)

# Task 1

walls, blocks, maxCoord, minCoord = solve1()
surfaces = { key:val for key, val in walls.items() if val == 0}

print( 'Result Task 1: ', len(surfaces))

# Task 2


blocksToCheck = (minCoord[0] - 1, minCoord[1] - 1, minCoord[2] -1)
fill()

openSurfaces = { key:val for key, val in surfaces.items() if val == 1}

print( len(openSurfaces))