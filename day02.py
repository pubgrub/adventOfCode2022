# AdventOfCode 2022
# Day 02

#get input data
lines = []
with open( "02.data", "r") as file:
    for line in file:
        lines.append( line.strip())
file.close()

toWin = { 'A': 'Y', 'B': 'Z', 'C': 'X'}
toLose = { 'A': 'Z', 'B': 'X', 'C': 'Y'}

scores = {}
for i in list( 'ABC'):
    for j in list( 'XYZ'):
        points = ord(j) - 87
        if ord(j) - ord(i) == 23:
            points += 3
        elif toWin[i] == j:
            points += 6
        scores[ i + " " + j] = points

# Task 1

counts =  [ lines.count(l) * scores[ l] for l in set(lines)]

print( 'Result Task 1: ', sum(counts))

# Task 2
    
games = dict( (l, lines.count(l)) for l in set(lines))
score = 0
for str in games:
    (p1, p2) = str.split( ' ')
    if p2 == 'X':
        score += scores[ p1 + ' ' + toLose[ p1]] * games[str]
    if p2 == 'Y':
        score += scores[ p1 + ' ' + chr( ord(p1) + 23)] * games[str]
    if p2 == 'Z':
        score += scores[ p1 + ' ' + toWin[ p1]] * games[str]

print( 'Result Task 1: ', score)

