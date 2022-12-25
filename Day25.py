from helpers.importHelpers import *

getDecimal = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
getSNAFU = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}

stringInput = getInput()
requiredFuel = 0
for line in stringInput.split("\n"):
  for rank, digit in enumerate(line[-1::-1]):
    requiredFuel += getDecimal[digit] * 5**rank

highestRank = 0
highestNumberRepresentable = 0
while highestNumberRepresentable < requiredFuel: #2 is the highest value we can put every rank
  highestNumberRepresentable += 2 * 5**highestRank
  highestRank += 1

def getHighestNumberRepresentable(rank):
  number = 0
  while rank >= 0:
    number += 2 * 5**rank
    rank-=1
  return number

resultPart1 = ""
currentNumber = 0
for rank in range(highestRank-1, -1, -1):
  highestNumberBelow = getHighestNumberRepresentable(rank-1)
  if currentNumber + highestNumberBelow + 5**rank < requiredFuel:
    currentNumber += 2*5**rank
    resultPart1 += "2"
  elif currentNumber + highestNumberBelow < requiredFuel:
    currentNumber += 5**rank
    resultPart1 += "1"
  elif currentNumber - 5**rank + highestNumberBelow < requiredFuel:
    resultPart1 += "0"
  elif currentNumber + -2*5**rank + highestNumberBelow < requiredFuel:
    currentNumber += -5**rank
    resultPart1 += "-"
  else:
    currentNumber += -2*5**rank
    resultPart1 += "="

print("Part 1: ", resultPart1)
print("Part 2: ", 0)