# AdventOfCode 2022

DAY = '06'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'

with open( filename, "r") as file:
  line = file.readline().strip()
file.close()

def search( n):
  groups = [ line[i:i + n] for i in range( 0, len(line) - n + 1, 1)]
  for i, g in enumerate( groups):
    if len(''.join(set(g))) == len( g):
      return( i + n)

# Task 1

print( 'Result Task 1: ', search( 4))

# Task 2

print( 'Result Task 2: ', search( 14))