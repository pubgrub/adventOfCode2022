# AdventOfCode 2022

DAY = '07'
TEST = 1

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
    for line in file:
        lines.append( line.strip())
file.close()

root = { 'parent': '', 'size': 0, 'dirs': {} }
dir = {}
for l in lines:
    words = l.split(' ')
    if words[0] == '$':
        if words[1] == 'ls':
            continue
        # cd
        if words[2] == '/':
            dir = root
            size = 0 
        elif words[2] == '..':
            dir = dir['parent']
            dir['size'] += size
        else:
            dir = dir[ words[2]]
            size = 0
    elif words[0] == 'dir':
        dir['dirs'][words[1]] =  { 'parent': dir, 'size': 0, 'dirs':{}}
    else:
        dir['size'] += int(words[0])

print( root)