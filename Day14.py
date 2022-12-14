from helpers.importHelpers import *

def insertLine(line, caveMap):
  coords = line.split(" -> ")
  for i in range(len(coords)-1):
    x1, y1 = coords[i].split(",")
    x2, y2 = coords[i+1].split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    stepX = int((x2-x1)/abs(x2-x1)) if x2!=x1 else 1 # 1 or -1
    stepY = int((y2-y1)/abs(y2-y1)) if y2!=y1 else 1# 1 or -1
    for x in range(x1, x2+stepX, stepX):
      for y in range(y1, y2+stepY, stepY):
        caveMap.add((x,y))

def getCaveMap(stringInput):
  caveMap = set()
  for line in stringInput.split("\n"):
    insertLine(line, caveMap)
  return caveMap

def part1(caveMap, source = 500):
  sandInCave = 0
  maxDepth = max(caveMap, key=lambda x: x[1])[1]
  x = source
  y = 0
  while y < maxDepth:
    #look ahead where to go next
    if (x,y+1) in caveMap:
      if (x-1,y+1) not in caveMap:
        x -= 1
      elif (x+1,y+1) not in caveMap:
        x += 1
      else:
        caveMap.add((x,y))
        sandInCave += 1
        x = source
        y = -1
    y += 1
  return sandInCave

def part2(caveMap, source = 500):
  sandInCave = 0
  maxDepth = max(caveMap, key=lambda x: x[1])[1]
  floor = maxDepth + 2
  x = source
  y = 0
  while (source, 0) not in caveMap:
    #look ahead where to go next
    if (x,y+1) in caveMap or y+1 == floor:
      if (x-1,y+1) not in caveMap and y+1 != floor:
        x -= 1
      elif (x+1,y+1) not in caveMap and y+1 != floor:
        x += 1
      else:
        caveMap.add((x,y))
        sandInCave += 1
        x = source
        y = -1
    y += 1
  return sandInCave

stringInput = getInput()
print("Part 1: ", part1(getCaveMap(stringInput)))
print("Part 2: ", part2(getCaveMap(stringInput)))