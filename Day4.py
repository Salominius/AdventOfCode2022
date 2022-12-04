from helpers.importHelpers import *

def completelyIncludedIn(l1, r1, l2, r2):
  return l1 >= l2 and r1 <= r2

def overlap(l1, r1, l2, r2):
  return not (r1 < l2 or l1 > r2)

resultPart1 = 0
resultPart2 = 0
stringInput = getInput()
for line in stringInput.split("\n"):
  l1, r1, l2, r2 = [int(x) for x in line.replace("-", ",").split(",")]
  if completelyIncludedIn(l1, r1, l2, r2) or completelyIncludedIn(l2, r2, l1, r1):
    resultPart1 += 1

  if overlap(l1, r1, l2, r2):
    resultPart2 += 1  

print("Part 1: ", resultPart1)
print("Part 2: ", resultPart2)