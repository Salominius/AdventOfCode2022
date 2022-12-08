from helpers.importHelpers import *

def getRanges(treeRow, treeColumn, height, width): #returns 4 lists of tuples (row, column) for the 4 directions
  # tree -> right side:
  yield [(row, treeColumn) for row in range(treeRow+1, width)]
  # tree -> left side:
  yield [(row, treeColumn) for row in range(treeRow-1, -1, -1)]
  # tree -> top side:
  yield [(treeRow, column) for column in range(treeColumn-1, -1, -1)]
  # tree -> bottom side:
  yield [(treeRow, column) for column in range(treeColumn+1, height)]

def getVisibleTrees(trees):
  height = len(trees)
  width = len(trees[0])
  visibleTreesCounter = 2*height + 2*width - 4 #the trees on the edges are all visible
  for row in range(1, height - 1):
    for column in range(1, width - 1):
      # --- for every tree within the grid, we check if it is visible from the 4 directions ---
      for direction in getRanges(row, column, height, width): #for each direction, we check if there is a higher tree
        for eachCoordinate in direction:
          if trees[eachCoordinate[0]][eachCoordinate[1]] >= trees[row][column]:
            break #if a tree is higher than the current tree, stop checking this direction
        else: #if no break occured, that means the tree is visible from that direction
          visibleTreesCounter += 1  # so we add 1 to the counter,
          break                     # ... and we can stop checking the other directions
  return visibleTreesCounter

def getScenicScore(trees):
  height = len(trees)
  width = len(trees[0])
  maxScenicScore = 0
  for row in range(height):
    for column in range(width):
       # --- for every tree, we calculate its scenic score ---
      thisScenicScore = 1
      for direction in getRanges(row, column, height, width): #count how many trees are visible for each direction
        treesInDirection = 0
        for eachCoordinate in direction:
          treesInDirection += 1
          if trees[eachCoordinate[0]][eachCoordinate[1]] >= trees[row][column]:
            break
        thisScenicScore *= treesInDirection
      if thisScenicScore > maxScenicScore: #update max scenic score if nessecary
        maxScenicScore = thisScenicScore
  return maxScenicScore        
        
trees = [[int(digit) for digit in [*row]] for row in getInput().split("\n")]

print("Part 1: ", getVisibleTrees(trees))
print("Part 2: ", getScenicScore(trees))