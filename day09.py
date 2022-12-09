# AdventOfCode 2022

DAY = '09'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()

def solve( knots):
  x = [ 0 ] * knots 
  y = [ 0 ] * knots
  
  visited = [ (x[-1], y[-1])]

  for l in lines:
    dir, steps = l.split(' ')
    for s in range( 0, int(steps)):
      for k in range( 0, knots):
        if k == 0:
          if dir == 'R':
            x[k] += 1
          if dir == 'L':
            x[k] -= 1
          if dir == 'D':
            y[k] += 1
          if dir == 'U':
            y[k] -= 1
        else:
          if abs(x[k-1] - x[k]) == 2 or abs(y[k-1] - y[k]) == 2:
            if x[k-1] > x[k]:
              x[k] += 1
            if x[k-1] < x[k]:
              x[k] -= 1
            if y[k-1] > y[k]:
              y[k] += 1
            if y[k-1] < y[k]:
              y[k] -= 1
      visited.append( (x[k], y[k]))
  return len(set(visited))


# Task 1

print( 'Result Task 1: ', solve(2))

# Task 2

print( 'Result Task 2: ', solve(10))


