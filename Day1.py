from helpers.importHelpers import *

stringInput = getInput()

elves = []
for elf in stringInput.split("\n\n"):
  elves.append(0)
  for line in elf.splitlines():
    elves[-1]+=int(line)

print("Part 1: ", max(elves))
print("Part 2: ", sum(sorted(elves, reverse = True)[:3]))