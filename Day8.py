from helpers.importHelpers import *

def getVisibleTrees(trees):
  # 0 = not visible, 1 = visible
  visibleTrees = [[0 for _ in row] for row in trees]
  #left to right
  for row in range(len(trees)):
    visibleHeight = -1
    for column in range(len(trees[0])):
      if trees[row][column] > visibleHeight:
        visibleTrees[row][column] = 1
        visibleHeight = trees[row][column]
  # top to bottom
  for column in range(len(trees[0])):
    visibleHeight = -1
    for row in range(len(trees)):
      if trees[row][column] > visibleHeight:
        visibleTrees[row][column] = 1
        visibleHeight = trees[row][column]
  # right to left
  for row in range(len(trees)):
    visibleHeight = -1
    for column in range(len(trees[0])-1, -1, -1):
      if trees[row][column] > visibleHeight:
        visibleTrees[row][column] = 1
        visibleHeight = trees[row][column]
  # bottom to top
  for column in range(len(trees[0])-1, -1, -1):
    visibleHeight = -1
    for row in range(len(trees)-1, -1, -1):
      if trees[row][column] > visibleHeight:
        visibleTrees[row][column] = 1
        visibleHeight = trees[row][column]
  return visibleTrees 

def getScenicScore(trees):
  scenicScore =[[0 for _ in row] for row in trees]
  for row in range(len(trees)):
    for column in range(len(trees[0])):
      # --- check up, down, left, right ---

      # up
      directionScore = 0
      for up in range (1, row+1):
        directionScore += 1
        if trees[row-up][column] >= trees[row][column]:
          break
      scenicScore[row][column] = directionScore

      # down
      directionScore = 0
      for down in range (1, len(trees)-row):
        directionScore += 1
        if trees[row+down][column] >= trees[row][column]:
          break
      scenicScore[row][column] *= directionScore

      # left
      directionScore = 0
      for left in range (1, column+1):
        directionScore += 1
        if trees[row][column-left] >= trees[row][column]:
          break
      scenicScore[row][column] *= directionScore

      # right
      directionScore = 0
      for right in range (1, len(trees[0])-column):
        directionScore += 1
        if trees[row][column+right] >= trees[row][column]:
          break
      scenicScore[row][column] *= directionScore    
  return max(max(row) for row in scenicScore)
        
stringInput = getInput()
trees = [[int(char) for char in [*line]] for line in stringInput.split("\n")]

visibleTrees = getVisibleTrees(trees)
print("Part 1: ", sum(sum(visibleTrees, [])))
print("Part 2: ", getScenicScore(trees))