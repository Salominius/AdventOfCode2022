from helpers.importHelpers import *

def getValidNeighbors(heightMap, current, reversed):
  currentX, currentY = current
  directions = [(0,1), (0,-1), (1,0), (-1,0)]
  for x, y in directions:
    x += currentX
    y += currentY
    if x >= 0 and y >= 0 and x < len(heightMap[0]) and y < len(heightMap):
      if reversed:
        if heightMap[y][x]+1 >= heightMap[currentY][currentX]:
          yield (x, y)
      else:
        if heightMap[y][x] <= heightMap[currentY][currentX]+1:
          yield (x, y)

def bfs(heightMap, start, endFunc, reversed = False):
  queue = [start]
  visited = set()
  cost = {(start): 0}
  while queue:
    current = queue.pop(0)
    if endFunc(current): #endFunc(current) is true, if current is the goal
      return cost[current]
    for neighbor in getValidNeighbors(heightMap, current, reversed):
      if neighbor not in visited or cost[current] + 1 < cost[neighbor]:
        cost[neighbor] = cost[current] + 1
        queue.append(neighbor)
        visited.add(neighbor)

stringInput = getInput()
heightMap = []
chars = "abcdefghijklmnopqrstuvwxyz"
for y, line in enumerate(stringInput.split("\n"), 0):
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

print("Part 1: ", bfs(heightMap, start, lambda position: position == end))
print("Part 2: ", bfs(heightMap, end, lambda position: heightMap[position[1]][position[0]] == 0, reversed = True))