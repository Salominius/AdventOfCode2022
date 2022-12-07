from helpers.importHelpers import *

class Directory:
  def __init__(self, parent):
    self.parent = parent
    self.size = 0
    self.children = {}
  def addFile(self, size):
    self.size += size
    if self.parent != None:
      self.parent.addFile(size)

def sumSizeBelowLimit(directory, limit):
  sum = 0
  if directory.size <= limit:
    sum += directory.size
  for child in directory.children.values():
    sum += sumSizeBelowLimit(child, limit)
  return sum

def findSmallestDirToDelete(directory, spaceToFree):
  childCandidates = []
  for child in directory.children.values():
    if child.size > spaceToFree:
      childCandidates.append(findSmallestDirToDelete(child, spaceToFree))
  if len(childCandidates) == 0:
    return directory.size
  return min(childCandidates)  

stringInput = getInput()

root = Directory(None)
for line in stringInput.split("\n"):
  splittedLine = line.split(" ")
  match splittedLine[0]:
    case "$":
      if splittedLine[1] == "cd":
        match splittedLine[2]:
          case "..":
            currentDirectory = currentDirectory.parent
          case "/":
            currentDirectory = root
          case _:
            currentDirectory = currentDirectory.children[splittedLine[2]]
    case "dir":
      currentDirectory.children[splittedLine[1]] = Directory(currentDirectory)
    case _:
      currentDirectory.addFile(int(splittedLine[0]))

print("Part 1: ", sumSizeBelowLimit(root, 100000))
print("Part 2: ", findSmallestDirToDelete(root, spaceToFree = 30000000 - (70000000 - root.size)))