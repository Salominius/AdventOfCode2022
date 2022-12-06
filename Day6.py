from helpers.importHelpers import *

stringInput = getInput()

def findMarker(stringInput, markerLength):
  for i in range(len(stringInput)):
    if len(set(stringInput[i:i + markerLength])) == markerLength:
      return i+markerLength

print("Part 1: ", findMarker(stringInput, 4))
print("Part 2: ", findMarker(stringInput, 14))