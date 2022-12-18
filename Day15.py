from helpers.importHelpers import *
import re

def parseInput(stringInput = getInput()):
  for line in stringInput.split("\n"):
    yield map(int, re.findall(r"-?\d+", line))

def part1(y = 2000000):
  row = set()
  beaconsInRow = set()
  for x1, y1, x2, y2 in parseInput():
    manhattenDistance = abs(x1 - x2) + abs(y1 - y2)
    yDistance = abs(y1 - y)
    for width in range(manhattenDistance - yDistance + 1):
      row.add(x1+width)
      row.add(x1-width)
    if y2 == y:
      beaconsInRow.add(x2)
  return len(row)-len(beaconsInRow)

def part2(limit = 4000000):
  scanners = []
  for x1, y1, x2, y2 in parseInput():
    manhattenDistance = abs(x1 - x2) + abs(y1 - y2)
    scanners.append((x1, y1, manhattenDistance))

  for y in range(limit+1):
    x = 0
    while x <= limit:
      for xScanner, yScanner, vision in scanners:
        distance = abs(y-yScanner) + abs(x-xScanner) #distance to scanner
        if distance <= vision: #scanner sees us if distance is less or equal to vision
          x = xScanner + vision - abs(y - yScanner) + 1 # set x to the right side of the scanner
          break
      else:
        return x*4000000+y
    y += 1

print("Part 1: ", part1())
print("Part 2: ", part2())