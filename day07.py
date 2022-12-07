# AdventOfCode 2022

DAY = '07'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
    for line in file:
        lines.append( line.strip())
file.close()

dirs = [ { 'parent': -1 , 'size': 0, 'subdirs': {} }]
actdir = 0
for l in lines:
    words = l.split(' ')
    if words[0] == '$':
        if words[1] == 'ls':
            continue
        # cd
        if words[2] == '/':
            actdir = 0
            size = 0 
        elif words[2] == '..':
            s = dirs[actdir]['size']
            actdir = dirs[actdir]['parent']
            dirs[actdir]['size'] += s
        else:
            actdir = dirs[actdir]['subdirs'][ words[2]]
            size = 0
    elif words[0] == 'dir':
        dirs.append( { 'parent': actdir, 'size': 0, 'subdirs':{} })
        dirs[actdir]['subdirs'][words[1]] =  len(dirs) - 1
    else:
        dirs[actdir]['size'] += int(words[0])

# add size of last dirs up to /
while dirs[actdir]['parent'] != -1:
    s = dirs[actdir]['size']
    actdir = dirs[actdir]['parent']
    dirs[actdir]['size'] += s

# for Task 1
sizeSum = 0

# for Task 2
spaceToClear = 30000000 - 70000000 + dirs[0]['size']
minValidSpace = 999999999

for d in dirs:
    if d['size'] <= 100000:
        sizeSum += d['size']
    if d['size'] >= spaceToClear and d['size'] < minValidSpace:
        minValidSpace = d['size']

# Task 1

print( 'Result Task 1: ', sizeSum)

# Task 2

print( 'Result Task 2: ', minValidSpace)
