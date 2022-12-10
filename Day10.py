from helpers.importHelpers import *

def drawPixel(pixelBeingDrawn, spritePosition):
  pixel = "" if pixelBeingDrawn%40 else "\n"
  if abs(pixelBeingDrawn%40 - spritePosition) <= 1:
    pixel += "\u2588"
  else:
    pixel += " "
  return pixel

def getOperations():
  for line in getInput().split("\n"):
    yield 0
    if line != "noop":
      yield int(line.split(" ")[1])  

resultPart1 = 0
resultPart2 = ""
registerX = 1
cycle = 0

for operation in getOperations():
  cycle += 1
  #cycle started
  if (cycle - 20)%40 == 0:
    resultPart1 += cycle*registerX
  resultPart2 += drawPixel(cycle-1, registerX)
  #cycle ended
  registerX += operation

print("Part 1: ", resultPart1)
print("Part 2: ", resultPart2)