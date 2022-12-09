from helpers.importHelpers import *

def getNormalizedDistance(distance):
  if distance == 0:
    return 0
  return distance/abs(distance)

def getTailPosition(oldTailPos, HeadPos):
  diffX = HeadPos[0] - oldTailPos[0]
  diffY = HeadPos[1] - oldTailPos[1]
  if abs(diffX) <= 1 and abs(diffY) <= 1:
    return oldTailPos

  diffX = getNormalizedDistance(diffX)
  diffY = getNormalizedDistance(diffY)
  return (oldTailPos[0] + diffX, oldTailPos[1] + diffY)

def getVisitedPositions(input, ropeLength):
  knots = [(0,0)] * ropeLength  #knots[0] is the head, knots[-1] is the tail
  visitedPositions = set()
  for line in stringInput.split("\n"):
    direction, distance = line.split(" ")
    distance = int(distance)
    match direction:
      case "R":
        diffX, diffY = 1, 0
      case "L":
        diffX, diffY = -1, 0
      case "U":
        diffX, diffY = 0, 1
      case "D":
        diffX, diffY = 0, -1

    for _ in range(distance):
      knots[0] = (knots[0][0] + diffX, knots[0][1] + diffY) #move head
      for j in range(1, len(knots)):  #move tail accordingly
        knots[j] = getTailPosition(knots[j], knots[j-1])
      visitedPositions.add(knots[-1])
  return(len(visitedPositions))

stringInput = getInput()  
print("Part 1: ", getVisitedPositions(stringInput, 2))
print("Part 2: ", getVisitedPositions(stringInput, 10))