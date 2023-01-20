import copy
# AdventOfCode 2022

DAY = '24'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

print( len(lines), len(lines[0]))

yWalkers = {}
xWalkers = {}

for y in range( 0, len(lines) - 2):
	xWalkers[y] = []
for x in range( 0, len(lines[0]) - 2):
	yWalkers[x] = []

for y, l in enumerate(lines):
	if y == 0:
		start = ( l.find( '.') -1, -1)
	elif y == len(lines) - 1:
		goal = ( l.find('.') -1, len(lines) - 2)
	else:
		for x in range( 1, len(l) - 1):
			char = l[x]
			if char == '.':
				continue
			if char in 'v>':
				dir = 1
			else:
				dir = -1				
			if char in '^v':
				yWalkers[x - 1].append( (y - 1,dir) )
			else:
				xWalkers[y - 1].append( (x - 1,dir) )
print( xWalkers)
print( yWalkers)
print( start, goal)
print( -5 % 4)

toDo = {(start, 1):''}
fastest = 99999
neighbors = [(0,0),(1,0),(0,1),(-1,0),(0,-1)]
minY = 0
maxY = len(lines) - 3
minX = 0
maxX = len(lines[0]) - 3

print( minX, maxX, minY, maxY)

done = {}
while toDo:
	((xPos, yPos), move) = list(toDo)[0]
	toDo.pop( ((xPos, yPos), move))
	if (xPos,yPos) == goal:
		fastest = min(fastest, move - 1)
		continue		
	if move > fastest:
		continue
	if ((xPos, yPos),move) in done:
		continue
	else:
		done[((xPos,yPos,),move)] = ''
	toCheck = {}
	for dx,dy in neighbors:
		x = xPos + dx
		y = yPos + dy
		if (x,y) == start or (x,y) == goal or ( x >= minX and  x <= maxX and y >= minY and y <= maxY):
			toCheck[(x,y)] = True
	#print( 'neighbors: ', toCheck)
	for cX in range( max(xPos - 1, minX), min(xPos + 1, maxX) + 1):
		#print( xPos, minX, maxX, cX)
		for (InitialWalkerY, walkerDir) in yWalkers[cX]:
			walkerY = (InitialWalkerY + move * walkerDir) % (maxY + 1)
			if ( cX, walkerY) in toCheck:
				toCheck.pop( (cX, walkerY))
			#print( 'ywalker:', InitialWalkerY, walkerDir, walkerY)
	for cY in range( max(yPos - 1, minY), min(yPos + 1, maxY) + 1):
		#print( yPos, minY, maxY, cY)		
		for (InitialWalkerX, walkerDir) in xWalkers[cY]:
			walkerX = (InitialWalkerX + move * walkerDir) % (maxX + 1)
			if ( walkerX,cY) in toCheck:
				toCheck.pop( (walkerX, cY))
			#print( 'Xwalker:', InitialWalkerX, walkerDir, walkerX)
	#print( 'valid Neighbors: ', toCheck)
	for newMoves in toCheck:
		toDo[newMoves, move + 1] = ''
	#print( 'new List to do: ', toDo)

print( fastest)
