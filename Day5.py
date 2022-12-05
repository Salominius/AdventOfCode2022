from collections import deque #faster than list-implementation
from helpers.importHelpers import *

def getStacks(initialState):
  numStacks = int(initialState[-1].strip().split(" ")[-1]) #last element of last line in initialState is number of stacks
  stacks = [deque() for _ in range(numStacks)]  #stacks = [[], [], []] (list containing numStacks sublists)
  for line in reversed(initialState[0:-1]):     #iterating backwards and skipping the last line (containing the numbers)
    for j in range(1, len(line), 4):            #starting with index 1, iterating by 4 (to skip "] [" between the numbers)
      if line[j] != " ":
        stacks[int((j-1)/4)].append(line[j])
  return stacks

stringInput = getInput(noStrip=True) #noStrip=True because I want the initialState to be the same as in the input file

initialState, instructions = stringInput.split("\n\n")
initialState = initialState.split("\n")
instructions = instructions.strip().split("\n")

def part1():
  stacks = getStacks(initialState)
  for line in instructions:
    amount, fromStack, toStack = [int(n) for n in line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")]
    for _ in range(amount):
      stacks[toStack-1].append(stacks[fromStack-1].pop())

  return "[" + "".join([stack[-1] for stack in stacks]) + "]"

def part2():
  stacks = getStacks(initialState)
  workingStack = deque()
  for line in instructions:
    amount, fromStack, toStack = [int(n) for n in line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")]
    for _ in range(amount):
      workingStack.append(stacks[fromStack-1].pop())
    for _ in range(amount):
      stacks[toStack-1].append(workingStack.pop())

  return "[" + "".join([stack[-1] for stack in stacks]) + "]"

print("Part 1: ", part1())
print("Part 2: ", part2())