import functools
from helpers.importHelpers import *

def compare(first, second):
  if type(first) == int and type(second) == int:
    return second - first
  if type(first) == list and type(second) == list:
    for eachElement, eachOtherElement in zip(first, second):
      comparision = compare(eachElement, eachOtherElement)
      if comparision != 0:
        return comparision
    return len(second) - len(first)
  if type(first) == int:
    return compare([first], second)
  return compare(first, [second])

def part1(stringInput):
  i = 1
  rightOrderCounter = 0
  x = iter(stringInput.replace("\n\n", "\n").split("\n"))
  for first, second in zip(x, x):
    first = eval(first)
    second = eval(second)
    if(compare(first, second)) > 0:
      rightOrderCounter += i
    i += 1
  return(rightOrderCounter)

def part2(stringInput):  
  sortedList = [[[2]], [[6]]]

  for line in stringInput.replace("\n\n", "\n").split("\n"):
    sortedList.append(eval(line))

  sortedList.sort(key=functools.cmp_to_key(compare), reverse=True)  
  return (sortedList.index([[6]]) + 1) * (sortedList.index([[2]]) + 1)


stringInput = getInput()
print("Part 1: ", part1(stringInput)) #5852
print("Part 2: ", part2(stringInput)) #24190