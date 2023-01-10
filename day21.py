import copy
# AdventOfCode 2022

DAY = '21'
TEST =0

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
codes = []

for l in lines:
  s = l.replace( ":", "").split( ' ')
  if len(s) == 2:
    solvedOrig[ s[0]] = int(s[1])
    if not s[0] in codes:
      codes.append( s[0])
  else:
    if s[0] == 'root':
      rootPart1 = s[1]
      rootPart2 = s[3]
    toDoOrig[ s[0]] = ([ s[1], s[3], s[2]])
    del s[2]
    for i in s:
      if not i in codes:
        codes.append( i)
      

def solve1( elem):
  if elem in solved:
    return solved[elem]
  else:
    op = toDo[elem][2]
    if op == '+':
      return( solve1( toDo[elem][0]) + solve1(toDo[elem][1]))
    elif op == '-':
      return( solve1( toDo[elem][0]) - solve1(toDo[elem][1]))
    elif op == '*':
      return( solve1( toDo[elem][0]) * solve1(toDo[elem][1]))
    elif op == '/':
      return( int(solve1( toDo[elem][0]) / solve1(toDo[elem][1])))

def solve2( elem, result):
  if elem == 'humn':
    return result
  else:
    for i in [ 0, 1]:
      if toDo[elem][i] in solved:
        solved_elem_value = solved[toDo[elem][i]]
      else:
        dep_elem = i
        dep_elem_value = toDo[elem][i]
    op = toDo[elem][2]
    if op == "=":
      return( solve2( dep_elem_value, solved_elem_value ))
    elif op == "+":
      return( solve2( dep_elem_value, result - solved_elem_value))      
    elif op == "-":
      if dep_elem == 0:
        return( solve2( dep_elem_value, result + solved_elem_value))      
      else:
        return( solve2( dep_elem_value, solved_elem_value - result))      
    elif op == "*":
      return( solve2( dep_elem_value, int( result / solved_elem_value)))      
    elif op == "/":
      if dep_elem == 0:
        return( solve2( dep_elem_value, result * solved_elem_value))      
      else:
        return( solve2( dep_elem_value, int( solved_elem_value / result)))      

# Task 1

toDo = copy.deepcopy( toDoOrig)
solved = copy.deepcopy( solvedOrig)

print( 'Result Task 1: ', solve1( 'root'))

# Task 2

toDo = copy.deepcopy( toDoOrig)
solved = copy.deepcopy( solvedOrig)

dep = ['humn']
indep = codes.copy()
indep.remove( 'humn')
solved.pop( 'humn')

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

# solve all indep into solved
for i in indep:
  solved[ i] = solve1( i)

toDo['root'][2] = '='

print( 'Result Task 2: ', solve2( 'root', 0))
