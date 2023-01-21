# AdventOfCode 2022

DAY = '25'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

value = { '2':2, '1':1, '0':0, '-':-1, '=':-2}
char =  {  2:'2', 1:'1', 0:'0', -1:'-', -2:'='}

def dec2Snafu( n):
  t = ''
  while n > 0:
    r = n % 5
    if r > 2:
      r -= 5
    elif r < -2:
      r += 5
    t += char[r]
    n = int((n - r) / 5)
  return (t[::-1])

totalSum = 0
for l in lines:
  le = len(l)
  sum = 0
  for i,c in enumerate(l):
    sum += 5 ** (le - i -1 ) * value[c]
  totalSum += sum

print( 'Result Task 1: ', dec2Snafu(totalSum))