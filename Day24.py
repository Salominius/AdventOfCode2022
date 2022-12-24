from helpers.importHelpers import *

# A few global variables: 
rBlizzards = []
dBlizzards = []
lBlizzards = []
uBlizzards = []

stringInput = getInput().split("\n")
width, height = len(stringInput[0]), len(stringInput)
myPositions = set([(1, 0)])
targetPosition = (width-2, height-1)

def loadBlizzards():
  for y in range(1, height - 1):
    for x in range(1, width - 1):
      match stringInput[y][x]:
        case ">":
          rBlizzards.append((x, y))
        case "<":
          lBlizzards.append((x, y))
        case "^":
          uBlizzards.append((x, y))
        case "v":
          dBlizzards.append((x, y))

def simulation():
  minute = 0
  while True:
    minute += 1
    # Move blizzards (Should definitely be improved)
    for index, blizzard in enumerate(rBlizzards):
      if blizzard[0] == width - 2:
        rBlizzards[index] = (1, blizzard[1])
      else:
        rBlizzards[index] = (blizzard[0] + 1, blizzard[1])
    for index, blizzard in enumerate(dBlizzards):
      if blizzard[1] == height - 2:
        dBlizzards[index] = (blizzard[0], 1)
      else:
        dBlizzards[index] = (blizzard[0], blizzard[1] + 1)
    for index, blizzard in enumerate(lBlizzards):
      if blizzard[0] == 1:
        lBlizzards[index] = (width - 2, blizzard[1])
      else:
        lBlizzards[index] = (blizzard[0] - 1, blizzard[1])
    for index, blizzard in enumerate(uBlizzards):
      if blizzard[1] == 1:
        uBlizzards[index] = (blizzard[0], height - 2)
      else:
        uBlizzards[index] = (blizzard[0], blizzard[1] - 1)
    
    for position in list(myPositions):
      for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newPosition = (position[0] + direction[0], position[1] + direction[1])
        if newPosition == targetPosition:
          return minute
        if newPosition not in rBlizzards + lBlizzards + uBlizzards + dBlizzards and newPosition[0] > 0 and newPosition[0] < width - 1 and newPosition[1] > 0 and newPosition[1] < height - 1:
          myPositions.add(newPosition)
      if position in rBlizzards + lBlizzards + uBlizzards + dBlizzards:
        myPositions.remove(position)

def part2():
  global myPositions, targetPosition # needed to modify global variables
  minutes = resultPart1
  myPositions = set([targetPosition])
  targetPosition = (1,0)
  minutes += simulation()
  myPositions = set([targetPosition])
  targetPosition = (width-2, height-1)
  return minutes + simulation()

loadBlizzards()
resultPart1 = simulation()
resultPart2 = part2()
print("Part 1: ", resultPart1)
print("Part 2: ", resultPart2)