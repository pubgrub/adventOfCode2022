import copy
# AdventOfCode 2022

DAY = '21'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

solvedOrig = {}
toDoOrig = {}

for l in lines:
  s = l.replace( ":", "").split( ' ')
  if len(s) == 2:
    solvedOrig[ s[0]] = int(s[1])
  else:
    if s[0] == 'root':
      rootPart1 = s[1]
      rootPart2 = s[3]
    toDoOrig[ s[0]] = ([ s[1], s[3], s[2]])
      

def solve1( elem):
  if elem in solved:
    return solved[elem]
  else:
    if toDo[elem][2] == '+':
      return( solve1( toDo[elem][0]) + solve1(toDo[elem][1]))
    elif toDo[elem][2] == '-':
      return( solve1( toDo[elem][0]) - solve1(toDo[elem][1]))
    elif toDo[elem][2] == '*':
      return( solve1( toDo[elem][0]) * solve1(toDo[elem][1]))
    elif toDo[elem][2] == '/':
      return( int(solve1( toDo[elem][0]) / solve1(toDo[elem][1])))

def getAllCodes(lines):
  codes = []
  for l in lines:
    s = l.replace( ":", "").split( ' ')
    if len(s) == 2:
      if not s[0] in codes:
        codes.append( s[0])
    else:
      del s[2]
      for i in s:
        if not i in codes:
          codes.append( i)
  return codes

# Task 1

toDo = copy.deepcopy( toDoOrig)
solved = copy.deepcopy( solvedOrig)

print( 'Task 1: ', solve1( 'root'))

# Task 2

toDo = copy.deepcopy( toDoOrig)
solved = copy.deepcopy( solvedOrig)

dep = ['humn']
indep = getAllCodes( lines)

# move dependent codes from indep to dep
done = False
while not done:
  done = True
  for d in dep:
    for t in toDo:
      if d in toDo[t] and t in indep:
        dep.append( t)
        indep.remove( t)
        done = False




print( len(indep), len(set(indep)))
print( len(dep), len(set(dep)))
print( dep)

exit()

humn = -1000
done = False
while not done:
  toDo = copy.deepcopy( toDoOrig)
  solved = copy.deepcopy( solvedOrig)
  humn += 1
  if humn % 100 == 0:
    print( humn)
  solved['humn'] = humn

  while len(toDo):
    toDelete = []
    for k, v in toDo.items():
      if not ( v[0] in solved  and v[1] in solved):
        continue
      else:
        if v[2] == '+':
          solved[k] = solved[ v[0]] + solved[ v[1]]
        elif v[2] == '-':
          solved[k] = solved[ v[0]] - solved[ v[1]]
        elif v[2] == '*':
          solved[k] = solved[ v[0]] * solved[ v[1]]
        elif v[2] == '/':
          solved[k] = int(solved[ v[0]] / solved[ v[1]])
        toDelete.append( k)
    for d in toDelete:
      toDo.pop( d)
  if solved[rootPart1] == solved[rootPart2]:
    done = True

print( 'Task 2: ', humn)




