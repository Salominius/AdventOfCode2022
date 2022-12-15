from helpers.importHelpers import *

def parseInput(stringInput = getInput()):
  for line in stringInput.split("\n"):
    x1, y1, x2, y2 = map(lambda x: int(x.split(",")[0]), line.replace(":", ",").split("=")[1:])
    yield (x1, y1, x2, y2)
  
def part1(y = 2000000):
  row = set()
  beaconsInRow = set()
  for x1, y1, x2, y2 in parseInput():
    euclidianDistance = abs(x1 - x2) + abs(y1 - y2)
    yDistance = abs(y1 - y)
    for width in range(euclidianDistance - yDistance + 1):
      row.add(x1+width)
      row.add(x1-width)
    if y2 == y:
      beaconsInRow.add(x2)
  return len(row)-len(beaconsInRow)

def part2(limit = 4000000):
  scanners = []
  for x1, y1, x2, y2 in parseInput():
    euclidianDistance = abs(x1 - x2) + abs(y1 - y2)
    scanners.append((x1, y1, euclidianDistance))

  y = 0
  while y < limit:
    x = 0
    while x < limit:
      for xScanner, yScanner, vision in scanners:
        distance = abs(y-yScanner) + abs(x-xScanner)
        if distance <= vision: #scanner sees us
          if x < xScanner:
            skip = vision - distance + vision - abs(y - yScanner) + 1
          else:
            skip = vision - distance + 1
          #print("scanner at", xScanner, yScanner, "with vision", vision, "sees", x, y, "skipping", skip, "steps")
          x += skip
          break
      else:
        return x*4000000+y
    y += 1

print("Part 1: ", part1())
print("Part 2: ", part2())