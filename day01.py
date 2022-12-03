# AdventOfCode 2022

DAY = '01'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
    for line in file:
        lines.append( line.strip())
file.close()

lines.append('')

calories = 0
calorieList = []
for l in lines:
  if l:
    calories += int( l)
  else:
    calorieList.append( calories)
    calories = 0

calorieList.sort( reverse = True)

#Task 1
print( 'Result Task 1: ', calorieList[0])

print( 'Result Task 2', sum( calorieList[:3]))