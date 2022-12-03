from helpers.importHelpers import *

def getPriority(char):
  if char.isupper():
    return ord(char) - ord("A") + 27
  else:
    return ord(char) - ord("a") + 1

stringInput = getInput()

# Part 1:
resultPart1 = 0
for line in stringInput.split("\n"):
  commonItem = ""
  left, right = line[:len(line)//2], line[len(line)//2:]
  for elem in left:
    if elem in right:
      commonItem = elem
      break

  resultPart1 += getPriority(commonItem)

#Part 2:
resultPart2 = 0
x = iter(stringInput.split("\n"))
for first, second, third in zip(x, x, x):
  commonItem = ""
  for elem in first:
    if elem in second and elem in third:
      commonItem = elem
      break

  resultPart2 += getPriority(commonItem)


print("Part 1: ", resultPart1)
print("Part 2: ", resultPart2)