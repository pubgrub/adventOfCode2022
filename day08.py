# AdventOfCode 2022

DAY = '08'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()

# Task 1

visible = []
maxX = len(lines[0]) - 1
maxY = len(lines) - 1

for y, l in enumerate(lines):
  maxHeight = -1
  for x, c in enumerate(l):
    if int(c) > maxHeight:
      visible.append( ( x, y))
      if int(c) == 9:
        break
      else:
        maxHeight = int(c)
  maxHeight =-1
  for x in range( maxX, -1, -1):
    c = int(l[x])
    if int(c) > maxHeight:
      visible.append( ( x, y))
      if int(c) == 9:
        break
      else:
        maxHeight = int(c)

for x in range( 0, maxX):
  maxHeight = -1
  for y, l in enumerate(lines):
    height = int(l[x])
    if height > maxHeight:
      visible.append( ( x, y))
      if height == 9:
        break
      else:
        maxHeight = height
  maxHeight =-1
  for y in range( maxY, -1, -1):
    l = lines[y]
    c = int(l[x])
    if int(c) > maxHeight:
      visible.append( ( x, y))
      if int(c) == 9:
        break
      else:
        maxHeight = int(c)

print( 'Result Task 1: ', len(set(visible)))

# Task 2

maxScore = 0
for y in range( 0, maxY + 1):
  for x in range( 0, maxX + 1):
    height = lines[y][x]
    multiScore = 1
    
    score = 0
    for y1 in range( y - 1, -1, -1):
      score += 1
      if lines[y1][x] >= height:
        break
    multiScore *= score
    
    score = 0
    for y1 in range( y + 1, maxY + 1):
      score += 1
      if lines[y1][x] >= height:
        break
    multiScore *= score

    score = 0
    for x1 in range( x - 1, -1, -1):
      score += 1
      if lines[y][x1] >= height:
        break
    multiScore *= score

    score = 0
    for x1 in range( x + 1, maxX + 1):
      score += 1
      if lines[y][x1] >= height:
        break
    multiScore *= score

    maxScore = max(maxScore, multiScore)

print( 'Result Task 2: ', maxScore)

