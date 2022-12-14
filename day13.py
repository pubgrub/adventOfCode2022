# AdventOfCode 2022

DAY = '13'
TEST = 1

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()
lines.append( '')

packets = []
for l in range(  0, len(lines) - 1, 3):
  packets.append( [lines[l], lines[l+1]])
  
for p in packets:
  print( p[0])
  print( p[1])
  print()
  