# AdventOfCode 2022

DAY = '10'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()

img =  [''] * 7

def calcSignal( cycle, signal, x):
  y = cycle // 40

  if cycle % 40 >= x - 1 and cycle % 40 <= x + 1:
    img[y] += '#'
  else: 
    img[y] += '.'
  cycle += 1
  if (cycle + 20) %40 == 0 and cycle <= 220:
    signal += cycle * x
  return ( cycle, signal)

signal = 0
cycle = 0
x = 1
for instr in lines:
  a  = list((instr).split(' '))
  ( cycle, signal) = calcSignal( cycle, signal, x)
  if len(a) > 1:
    ( cycle, signal) = calcSignal( cycle, signal, x)
    x += int(a[1])

# Task 1

print( 'Result Task 1: ', signal)

# Task 2

print( '\nResult Task 2: \n')

for i in img:
  print( i)