# AdventOfCode 2022
# Day 01

#get input data
lines = []
with open( "01.data", "r") as file:
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