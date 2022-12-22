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

      			[0b00001000,
       			 0b00001000,
       			 0b00111000],

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

def solve():
	towerHeight = 1
	numBricks = 0
	rows = [bottomRow]
	lastFilledRow = 0
	arrowPos = -1
	brickPos = -1
	action = NEWBRICK
	brick = []

	while True:
		if numBricks == 2022:
			break
		if action == NEWBRICK:
			brickPos += 1
			if brickPos == len(bricks):
				brickPos = 0
			brickY = lastFilledRow + 4
			rowsToCreate =   brickY + len(bricks[ brickPos]) - (len(rows) - 1)
			for i in range(0, rowsToCreate):
				rows.append(emptyRow)
			brick = bricks[brickPos].copy()				
			#print( brick)
			action = HORIZONTAL
#			draw(rows)

		elif action == HORIZONTAL:
			arrowPos += 1
			if arrowPos == len(arrows):
				arrowPos = 0
			dir = 2 if arrows[arrowPos] == '<' else 0.5
			#print( dir)
			collision = False
			for i,b in enumerate(brick):
				if int(b * dir) & rows[ brickY + i]:
					collision = True
			if not collision:
				for i,b in enumerate(brick):
					brick[i] = int( brick[i] * dir)
#				draw(rows)

			action = VERTICAL

		elif action == VERTICAL:
			collision = False
			for i,b in enumerate(brick):
				if b  & rows[ brickY + i - 1]:
					collision = True
			if not collision:
				brickY -= 1
				action = HORIZONTAL
			else:
				for i,b in enumerate( brick):
					rows[brickY + i] |= b
				for i in range( len(rows)-1 , -1, -1):
					if rows[i] != emptyRow:
						lastFilledRow = i
						break
				towerHeight = lastFilledRow
				print( towerHeight)
				numBricks += 1
				action = NEWBRICK	
				draw(rows)

	print( '***',len(rows))
	return towerHeight
				
def draw(rows):
	for i in range( len(rows) -1, -1, -1):
		print(format( rows[i], 'b'))
	print( "*****")

result = solve()
print( result)

