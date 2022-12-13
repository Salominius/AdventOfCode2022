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
  counter = 0
  i = 1
  x = iter(stringInput)
  for first, second in zip(x,x):
    if compare(eval(first), eval(second)) > 0:
      counter += i
    i += 1  
  return counter

def part2(stringInput):  
  sortedList = [[[2]], [[6]]]

  for line in stringInput:
    sortedList.append(eval(line))

  sortedList.sort(key=functools.cmp_to_key(compare), reverse=True)  
  return (sortedList.index([[6]]) + 1) * (sortedList.index([[2]]) + 1)


stringInput = getInput().replace("\n\n", "\n").splitlines()
print("Part 1: ", part1(stringInput)) #5852
print("Part 2: ", part2(stringInput)) #24190