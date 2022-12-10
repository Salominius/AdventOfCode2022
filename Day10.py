from helpers.importHelpers import *

def drawPixel(pixelDrawn, spritePosition):
  pixel = "" if pixelDrawn%40 else "\n"
  if abs(pixelDrawn%40 - spritePosition) <= 1:
    pixel += "\u2588"
  else:
    pixel += " "
  return pixel  

stringInput = getInput()

resultPart1 = 0
resultPart2 = ""
registerX = 1
cycle = 0
operationQueue = []
pixelDrawn = 0

for line in stringInput.split("\n"):
  operationQueue.append(0)
  if line != "noop":
    operationQueue.append(int(line.split(" ")[1]))

for operation in operationQueue:
  cycle += 1
  #cycle started
  if (cycle - 20)%40 == 0:
    resultPart1 += cycle*registerX
  resultPart2 += drawPixel(pixelDrawn, registerX)
  #cycle ended
  registerX += operation
  pixelDrawn += 1

print("Part 1: ", resultPart1)
print("Part 2: ", resultPart2)