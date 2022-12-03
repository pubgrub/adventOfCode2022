# AdventOfCode 2022

DAY = '03'
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

sum = 0
for line in lines:
  s = [set(line[i:i+len(line) // 2]) for i in range( 0, len( line), len(line)//2)]
  char = ord(s[0].intersection( s[1]).pop())
  char -= 96 if char >= 97 else 38
  sum += char

print( 'Result Task 1: ', sum)

# Task 2

sum = 0
groups =  [lines[i:i+3] for i in range( 0, len(lines), 3)]
for g in groups:
  char = ord(set(g[0]).intersection( set(g[1])).intersection(set(g[2])).pop())
  char -= 96 if char >= 97 else 38
  sum += char

print( 'Result Task 2: ', sum)