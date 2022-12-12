from helpers.importHelpers import *

def getValidNeighbors(heightMap, current):
  x, y = current
  if x > 0 and heightMap[y][x-1] <= heightMap[y][x]+1:
    yield (x-1, y)
  if x < len(heightMap[y])-1 and heightMap[y][x+1] <= heightMap[y][x]+1:
    yield (x+1, y)
  if y > 0 and heightMap[y-1][x] <= heightMap[y][x]+1:
    yield (x, y-1)
  if y < len(heightMap)-1 and heightMap[y+1][x] <= heightMap[y][x]+1:
    yield (x, y+1)

def bfs(heightMap, start, end):
  queue = [start]
  visited = set()
  cost = {(start): 0}
  while queue:
    current = queue.pop(0)
    if current == end:
      continue
    for neighbor in getValidNeighbors(heightMap, current):
      if neighbor not in visited or cost[current] + 1 < cost[neighbor]:
        cost[neighbor] = cost[current] + 1
        queue.append(neighbor)
        visited.add(neighbor)
  return cost

stringInput = getInput()
heightMap = []
for y, line in enumerate(stringInput.split("\n"), 0):
  chars = "abcdefghijklmnopqrstuvwxyz"
  heightMap.append([])
  for x, char in enumerate(line, 0):
    match char:
      case "S":
        start = (x,y)
        heightMap[y].append(0) #value of a
      case "E":
        end = (x,y)
        heightMap[y].append(25) #value of z
      case _:
        heightMap[y].append(chars.index(char))


def bfs2(heightMap, start, end):
  queue = [start]
  visited = set()
  cost = {(start): 0}
  while queue:
    current = queue.pop(0)
    for neighbor in getValidNeighbors2(heightMap, current):
      if neighbor not in visited or cost[current] + 1 < cost[neighbor]:
        cost[neighbor] = cost[current] + 1
        queue.append(neighbor)
        visited.add(neighbor)
  return cost

def getValidNeighbors2(heightMap, current):
  x, y = current
  if x > 0 and heightMap[y][x] <= heightMap[y][x-1]+1:
    yield (x-1, y)
  if x < len(heightMap[y])-1 and heightMap[y][x] <= heightMap[y][x+1]+1:
    yield (x+1, y)
  if y > 0 and heightMap[y][x] <= heightMap[y-1][x]+1:
    yield (x, y-1)
  if y < len(heightMap)-1 and heightMap[y][x] <= heightMap[y+1][x]+1:
    yield (x, y+1)  

def part2(end, start):
  cost = bfs2(heightMap, end, start)
  print(len(cost))
  costs = []
  for y, line in enumerate(heightMap):
    for x, char in enumerate(line):
      if char == 0 and (x,y) in cost:
        costs.append(cost[(x,y)])
  return min(costs)

print("Part 1: ", bfs(heightMap, start, end)[end])
print("Part 2: ", part2(end, start))