# AdventOfCode 2022

import copy

DAY = '05'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
    for line in file:
        lines.append( line)
file.close()

#find sizes
for i, l in enumerate( lines):
  if l[1] == '1':
    maxStackHeight = i
    procedureStartsAt = i + 2
    break
  
#load stacks
stacks = [ ]
for l in reversed( lines[0:maxStackHeight]):
  for i, item in enumerate([ l[i:i+4].strip() for i in range( 0, len(l), 4)]):
    if item:
      if len(stacks) > i:
        stacks[i].append( list(item)[1])
      else:
        stacks.append([list(item)[1]])

#load procedure
moveCount = []
moveFrom = []
moveTo = []
for s in lines[procedureStartsAt:]:
  (dummy, moveC, dummy, moveF, dummy, moveT ) = s.strip().split( ' ')  
  moveCount.append( int(moveC))
  moveFrom.append( int(moveF ) - 1)
  moveTo.append( int(moveT) - 1)

# Task 1
stack1 = copy.deepcopy(stacks)
for i, p in enumerate( moveCount):
  stack1[moveTo[i]].extend( list(reversed(stack1[moveFrom[i]][len(stack1[moveFrom[i]]) - p:])))  
  stack1[moveFrom[i]] = stack1[moveFrom[i]][0: len(stack1[moveFrom[i]]) - p]
message = [ stack1[i][-1] for i in range( 0, len(stack1))]

print( 'Result Task 1: ', ''.join(message))

# Task 2
for i, p in enumerate( moveCount):
  stacks[moveTo[i]].extend( stacks[moveFrom[i]][len(stacks[moveFrom[i]]) - p:])  
  stacks[moveFrom[i]] = stacks[moveFrom[i]][0: len(stacks[moveFrom[i]]) - p]
message = [ stacks[i][-1] for i in range( 0, len(stacks))]

print( 'Result Task 2: ', ''.join(message))