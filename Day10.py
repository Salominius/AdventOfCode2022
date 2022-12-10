from helpers.importHelpers import *

def drawPixel(pixelDrawn, spritePosition):
  if pixelDrawn % 40 == 0:
    print("")
  if abs(pixelDrawn%40 - spritePosition) <= 1:
    print("\u2588", end = "")
  else:
    print(" ", end = "")

stringInput = getInput()

resultPart1 = 0
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
  drawPixel(pixelDrawn, registerX)
  #cycle ended
  registerX += operation
  pixelDrawn += 1

print("")
print("Part 1: ", resultPart1)