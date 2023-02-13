# AdventOfCode 2022

DAY = '20'
TEST = 1

#get input data
if TEST == 1:
  testStr = 'test'
elif TEST == 2:
  testStr = 'mytest'
else:
  testStr = ''
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

print( nList)
for i in order:
  idx = nList.index( i)
  if i != 0:
    nList.pop( idx)
    if i > 0:
      newIdx = (idx + i ) % (len(nList) )
    elif i < 0:
      newIdx = (idx + i ) % (len(nList) ) 
    nList.insert( newIdx , i)
  else:
    newIdx = idx
  if TEST:
    print( i, idx, newIdx, nList)
  
zIdx = nList.index(0) 
sum = 0
print( zIdx)
for i in range( 1,4):
  print( zIdx + i * 1000, nList[(zIdx + 1000 * i) % len(nList)])
  sum +=  nList[(zIdx + 1000 * i) % len(nList)]
print( sum) 