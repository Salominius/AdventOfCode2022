from helpers.importHelpers import *

def getCubes(stringInput):
  return [tuple(map(int, line.split(","))) for line in stringInput.split("\n")]

def touching(cube1, cube2):
  return abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2]) == 1

def getSourroundingFields(position):
  x, y, z = position
  return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]

def part1(cubes):
  surfaceArea = 6*len(cubes) #calculate surface area of all cubes (6 faces per cube)
  for i in range(len(cubes)):
    for j in range(i+1, len(cubes)):
      if touching(cubes[i], cubes[j]):
        surfaceArea-=2  #if two cubes are touching, the surface area is reduced by 2
  return surfaceArea

def part2(cubes):
  # Define bounding box for the cubes
  minX = min([cube[0] for cube in cubes])-1
  maxX = max([cube[0] for cube in cubes])+1
  minY = min([cube[1] for cube in cubes])-1
  maxY = max([cube[1] for cube in cubes])+1
  minZ = min([cube[2] for cube in cubes])-1
  maxZ = max([cube[2] for cube in cubes])+1
  # Find all water outside the cubes using floodfill
  water = floodFill(minX, maxX, minY, maxY, minZ, maxZ, cubes, (maxX, maxY, maxZ), set())
  # Increase surface area each time a cube touches water
  surfaceArea = 0
  for i in range(len(cubes)):
    for neighbour in getSourroundingFields(cubes[i]):
      if neighbour in water:
        surfaceArea+=1
  return surfaceArea

#iterative floodfill because the recursive version exceeded the recursion limit
def floodFill(minX, maxX, minY, maxY, minZ, maxZ, cubes, currentField, visitedFields):
  stack = []
  stack.append(currentField)
  while len(stack) > 0:
    currentField = stack.pop()
    if currentField not in cubes and currentField not in visitedFields:
      visitedFields.add(currentField)
      for x, y, z in getSourroundingFields(currentField):
        if (minX <= x <= maxX) and (minY <= y <= maxY) and (minZ <= z <= maxZ):
          stack.append((x, y, z))
  return visitedFields

cubes = getCubes(getInput())
print("Part 1: ", part1(cubes))
print("Part 2: ", part2(cubes))