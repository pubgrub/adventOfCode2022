# AdventOfCode 2022

DAY = '20'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

nList = []
done = {}
m = 0
for l in lines:
  n = int(l)
  nList.append(n)
  

order = nList.copy()

for i in order:
  idx = nList.index( i)
  if i != 0:
    nList.pop( idx)
    if i > 0:
      newIdx = (idx + i ) % (len(order) )
    elif i < 0:
      newIdx = (idx + i - 1) % (len(order) ) 
    nList.insert( newIdx + 1, i)
  #print( i, idx, newIdx, nList)
  
zIdx = nList.index(0) 
sum = 0
for i in range( 1,4):
  print( zIdx + i * 1000, nList[(zIdx + 1000 * i) % len(nList)])
  sum +=  nList[(zIdx + 1000 * i) % len(nList)]
print( sum) 