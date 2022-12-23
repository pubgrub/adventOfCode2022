import time
# AdventOfCode 2022

DAY = '17'
TEST = 1

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

arrows = lines[0]

bricks = [  [0b00111100],
			
						[0b00010000,
			 			 0b00111000,
			 			 0b00010000],

						[0b00111000,
			 			 0b00001000,
			 			 0b00001000],

						[0b00100000,
			 			 0b00100000,
			 			 0b00100000,
			 			 0b00100000],

						[0b00110000,
						 0b00110000] 
		]

emptyRow =  0b100000001
bottomRow = 0b111111111

NEWBRICK = 0
HORIZONTAL = 1
VERTICAL = 2

def solve( lastBrick):
	towerHeight = 1
	numBricks = 0
	rows = [bottomRow]
	lastFilledRow = 0
	arrowPos = -1
	brickPos = -1
	action = NEWBRICK
	brick = []

	while True:
		if numBricks == lastBrick:
			break
		if action == NEWBRICK:
			brickPos += 1
			if brickPos == len(bricks):
				brickPos = 0
			brickY = lastFilledRow + 4
			rows += [emptyRow] * ( brickY + len(bricks[ brickPos]) - (len(rows) - 1))
			brick = bricks[brickPos].copy()				
			action = HORIZONTAL

		elif action == HORIZONTAL:
			arrowPos += 1
			if arrowPos == len(arrows):
				arrowPos = 0
			collision = False
			if arrows[arrowPos] == '<':
				for i,b in enumerate(brick):
					if b + b & rows[ brickY + i]:
						collision = True
						break
				if not collision:
					for i in range( 0, len( brick)):
						brick[i] += brick[i]
			else:	
				for i,b in enumerate(brick):
					if b >> 1 & rows[ brickY + i]:
						collision = True
						break
				if not collision:
					for i in range( 0, len( brick)):
						brick[i] >>= 1
	 
			action = VERTICAL

		elif action == VERTICAL:
			collision = False
			for i,b in enumerate(brick):
				if b & rows[ brickY + i - 1]:
					collision = True
					break
			if not collision:
				brickY -= 1
				action = HORIZONTAL
			else:
				for i,b in enumerate( brick):
					rows[brickY + i] |= b
				lastFilledRow = max( lastFilledRow, brickY + len(brick) - 1)
				numBricks += 1
				action = NEWBRICK	

	return lastFilledRow
				
# Task 1

result = solve( 2022)
print( "Result Task 1: ", result)


