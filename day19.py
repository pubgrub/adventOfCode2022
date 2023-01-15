import re, time
# AdventOfCode 2022

DAY = '19'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
	for line in file:
		lines.append( line.strip())
file.close()

ORE = 0
CLAY = 1
OBS = 2
GEO = 3

pattern = re.compile( r".*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)")

def mine( inv, bots):
  inv2 = inv.copy()
  for i in range( 0, len(inv)):
    inv2[i] += bots[i]
  return inv2   

def buildBot( type, inv, bots):
  inv2 = inv.copy()
  for ore, amount in costs[type].items():
    inv2[ore] -= amount
  bots2 = list(bots)
  bots2[type] += 1
  return inv2, tuple(bots2)
  
def advance(inv, bots, time):
  global maxGeodes
  if ( tuple(inv), tuple(bots), time) in seen:
    return 
  else:
    seen[ tuple(inv), tuple(bots), time] = maxGeodes
  maxGeodes = max( maxGeodes, inv[GEO])

  if time > 0:
    for i in range( len(inv) - 1, -1, -1):
      canAfford = True
      for ore, amount in costs[i].items():
        if inv[ore] < amount:
          canAfford = False
          break
      if canAfford:
        new_inv = mine( inv, bots)
        if time >= 4 or ( time == 3 and i != CLAY) or ( time == 2 and i == GEO):
          new_inv, new_bots = buildBot( i, new_inv, bots)    
          if i == GEO:
            if new_bots[GEO] in minTimeGeoBots:
              if minTimeGeoBots[new_bots[GEO]] > time:
                return
              elif minTimeGeoBots[new_bots[GEO]] < time:
                minTimeGeoBots[new_bots[GEO]] = time      
            else:
              minTimeGeoBots[new_bots[GEO]] = time
            
          advance( new_inv, new_bots, time - 1) 
        else:
          maxGeodes = max( maxGeodes, inv[GEO])
    new_inv = mine( inv, bots)     
    
    advance( new_inv, bots, time - 1)
  return     

#Task 1

inv = [0, 0, 0, 0] 
bots = (1, 0, 0, 0)
costs = { 0: {0:0}, 1: {0:0}, 2: {0:0, 1:0}, 3: {0:0, 2:0} }

score = 0
for l in lines:
  x = re.match( pattern, l )
  id, costs[0][0], costs[1][0], costs[2][0], costs[2][1], costs[3][0], costs[3][2]  = tuple( int(i) for i in list(x.groups()))

  print( costs)

  maxGeodes = 0
  seen = {}
  steps = 24

  minTimeGeoBots = {}
  minTimeObs = {}
  minTimeClay = {}

  t1 = time.time()
  advance( inv, bots, steps)
  score += maxGeodes * id
  print( time.time() - t1, id, maxGeodes, score)

# Task 2

# inv = [0, 0, 0, 0] 
# bots = (1, 0, 0, 0)
# costs = { 0: {0:0}, 1: {0:0}, 2: {0:0, 1:0}, 3: {0:0, 2:0} }

# score = 1
# for l in lines[0:3]:
#   x = re.match( pattern, l )
#   id, costs[0][0], costs[1][0], costs[2][0], costs[2][1], costs[3][0], costs[3][2]  = tuple( int(i) for i in list(x.groups()))

#   print( costs)

#   maxGeodes = 0
#   seen = {}
#   steps = 32

#   minTimeGeo = {}
#   minTimeObs = {}
#   minTimeClay = {}

#   t1 = time.time()
#   advance( inv, bots, steps)
#   score *= maxGeodes
#   print( time.time() - t1, id, maxGeodes, score)

