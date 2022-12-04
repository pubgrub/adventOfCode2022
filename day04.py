# AdventOfCode 2022

DAY = '04'
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

count1 = 0
count2 = 0
for l in lines:
  ( e1, e2) = l.split(',')
  ( x1, y1) = [ int(e) for e in e1.split('-')]
  ( x2, y2) = [ int(e) for e in e2.split('-')]
  if (x1 <= x2 and y1 >= y2) or ( x1 >= x2 and y1 <= y2):
    count1 += 1
  if (x1 >= x2 and x1 <= y2) or ( y1 >= x2 and y1 <= y2) or ( x2 >= x1 and x2 <= y1) or ( y2 >= x1 and y2 <= y1):
    count2 += 1

print( 'Result Task 1: ', count1)

print( 'Result Task 2: ', count2)
