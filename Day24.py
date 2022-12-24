from helpers.importHelpers import *

# A few global variables: 
def getBlizzards(stringInput, width, height): # blizzards = list(tuple(startX, startY, movingDirection))
  blizzards = []
  blizzardDirections = {'<': (-1,0), '>': (1,0), '^': (0,-1), 'v': (0,1)}
  for y in range(1, height - 1):
    for x in range(1, width - 1):
      if stringInput[y][x] != '.':
        blizzards.append((x, y, blizzardDirections[stringInput[y][x]]))
  return blizzards

def simulation(blizzards, start, targetPosition, minute = 0):
  myPositions = set([start])
  while True:
    minute += 1

    currentBlizzardPositions = set()
    for x,y,(dx,dy) in blizzards:
      currentBlizzardPositions.add((1 + (x-1+dx*minute)%(width-2), 1 + (y-1+dy*minute)%(height-2)))
    
    for position in list(myPositions):
      for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newPosition = (position[0] + direction[0], position[1] + direction[1])
        if newPosition == targetPosition:
          return minute
        if newPosition not in currentBlizzardPositions and newPosition[0] > 0 and newPosition[0] < width - 1 and newPosition[1] > 0 and newPosition[1] < height - 1:
          myPositions.add(newPosition)
      if position in currentBlizzardPositions:
        myPositions.remove(position)

stringInput = getInput().split("\n")
width, height = len(stringInput[0]), len(stringInput)
blizzards = getBlizzards(stringInput, width, height)
start = (1, 0)
target = (width-2, height-1)

print("Part 1: ", resultPart1 := simulation(blizzards, start, target))
print("Part 2: ", simulation(blizzards, start, target, simulation(blizzards, target, start, resultPart1)))