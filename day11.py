# AdventOfCode 2022

DAY = '11'
TEST = 0

#get input data
testStr = 'test' if TEST else ''
filename = "data/" + DAY + testStr + '.data'
lines = []

with open( filename, "r") as file:
  for line in file:
    lines.append( line.strip())
file.close()

def solve1( rounds):
  monkeys = []
  for l in lines:
    if len(l) == 0:
      continue
    w = l.split(' ')
    if w[0] == 'Monkey':
      monkeys.append({})
    if w[0] == 'Starting':
      monkeys[-1]['items'] = list(  int( v.replace(',','')) for v in w[2:]  )
    if w[0] == 'Operation:':
      monkeys[-1]['op'] = w[-2]
      if w[-1] == 'old':
        monkeys[-1]['oldOpVal'] = True
      else:
        monkeys[-1]['oldOpVal'] = False      
        monkeys[-1]['opVal'] = int(w[-1])
    if w[0] == 'Test:':
      monkeys[-1]['div'] = int(w[-1])      
    if w[1] == 'true:':
      monkeys[-1]['target'] = [int(w[-1])]      
    if w[1] == 'false:':
      monkeys[-1]['target'].append(int(w[-1]))

  inspected = [ 0] * len(monkeys)
  for r in range( 0, rounds):
    for x, m in enumerate(monkeys):
      for i in m['items']:
        worry = i
        if m['oldOpVal']:
          opVal = i
        else:
          opVal = m['opVal']
        if m['op'] == '*':
          worry *= opVal
        elif m['op'] == '+':
          worry += opVal
        worry //= 3
        target = m['target'][0] if worry % m['div'] == 0 else m['target'][1]
        inspected[ x] += 1
        monkeys[target]['items'].append( worry)
      monkeys[x]['items'] = []
  return inspected

def solve2( rounds):
  monkeys = []
  itemRests = []
  items = [] 
  for l in lines:
    if len(l) == 0:
      continue
    w = l.split(' ')
    if w[0] == 'Monkey':
      monkeys.append({ 'items': [] })
    if w[0] == 'Starting':      
      for i in list(  int( v.replace(',','')) for v in w[2:]  ):
        items.append( i)
        itemRests.append([])
        monkeys[-1]['items'].append( len(items) - 1)
    if w[0] == 'Operation:':
      monkeys[-1]['op'] = w[-2]
      if w[-1] == 'old':
        monkeys[-1]['oldOpVal'] = True
      else:
        monkeys[-1]['oldOpVal'] = False      
        monkeys[-1]['opVal'] = int(w[-1])
    if w[0] == 'Test:':
      monkeys[-1]['div'] = int(w[-1])      
    if w[1] == 'true:':
      monkeys[-1]['target'] = [int(w[-1])]      
    if w[1] == 'false:':
      monkeys[-1]['target'].append(int(w[-1]))
  
  for i in range( 0, len(itemRests)):
    for m in monkeys:
      itemRests[i].append( items[i] % m['div'])

  inspected = [ 0] * len(monkeys)
  for r in range( 0, rounds):
    for x, m in enumerate(monkeys):
      for i in m['items']:
        for j in range( 0, len(monkeys)):
          worry = itemRests[ i][j]
          if m['oldOpVal']:
            opVal = worry
          else:
            opVal = m['opVal']
          if m['op'] == '*':
            worry *= opVal
          elif m['op'] == '+':
            worry += opVal
          itemRests[i][j] = worry % monkeys[j]['div']
        target = m['target'][0] if itemRests[i][x] == 0 else m['target'][1]
        inspected[ x] += 1
        monkeys[target]['items'].append( i)
      monkeys[x]['items'] = []
  return inspected

result = solve1( 20)
result.sort( reverse = True)

print( 'Result Task 1: ', result[0] * result[1])

result = solve2( 10000)
result.sort( reverse = True)

print( 'Result Task 2: ', result[0] * result[1])

