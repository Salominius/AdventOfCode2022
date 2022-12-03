from helpers.importHelpers import *

enemyMovePoints = {"A": 1, "B": 2, "C": 3}
myMovePoints = {"X": 1, "Y": 2, "Z": 3}
myMoves = {1: "X", 2: "Y", 3: "Z"}

def getWinningMove(enemyMove):
  return myMoves.get(enemyMovePoints.get(enemyMove) + 1, "X")

def getDraw(enemyMove):
  return myMoves.get(enemyMovePoints.get(enemyMove))

def getLosingMove(enemyMove):
  return myMoves.get(enemyMovePoints.get(enemyMove) - 1, "Z")

def calculatePoints(myMove, enemyMove):
  result = myMovePoints.get(myMove)
  if myMovePoints.get(myMove) == enemyMovePoints.get(enemyMove) + 1 or myMovePoints.get(myMove) == enemyMovePoints.get(enemyMove) - 2:
    result += 6
  elif myMovePoints.get(myMove) == enemyMovePoints.get(enemyMove):
    result += 3
  return result

resultPart1 = 0
resultPart2 = 0
stringInput = getInput()
for line in stringInput.split("\n"):
  enemy, me = line.split(" ")

  resultPart1 += calculatePoints(me, enemy)

  if me == "X":
    me = getLosingMove(enemy)
  elif me == "Y":
    me = getDraw(enemy)
  elif me == "Z":
    me = getWinningMove(enemy)

  resultPart2 += calculatePoints(me, enemy)


print("Part 1: ", resultPart1)
print("Part 2: ", resultPart2)