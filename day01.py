# AdventOfCode 2022
# Day 01

#get input data
lines = []
with open( "data/01.data", "r") as file:
    for line in file:
        lines.append( line.strip())
file.close()

lines.append('')
calories = 0
maxCalories = [ 0, 0, 0]
for l in lines:
  if l:
    calories += int( l)
  else:
    for i, m in enumerate( maxCalories):
      if calories >= m:
        maxCalories.insert( i, calories)
        maxCalories.pop()
        break
    calories = 0

#Task 1
print( 'Result Task 1: ', maxCalories[0])

print( 'Result Task 2', sum( maxCalories))