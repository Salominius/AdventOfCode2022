from helpers.importHelpers import *
from math import lcm # get the least common multiple of a list of numbers

class Monkey:
  def __init__(self, startingItems, operationString, testString, testNumber):
    self.items = startingItems
    self.operation = lambda old: eval(operationString)
    self.test = lambda item: eval(testString)
    self.inspectedItems = 0
    self.testNumber = testNumber

  def inspect(self, worryReduction):
    self.items = [worryReduction(self.operation(item)) for item in self.items]

def getMonkeys(stringInput):
  monkeys = []
  x = iter(stringInput.replace("\n\n", "\n").split("\n"))
  for monkeyLine, itemsLine, operationLine, testLine, ifTrueLine, ifFalseLine in zip(x, x, x, x, x, x):
    items = []
    for item in itemsLine.strip().replace(",", "").split(" ")[2:]:
      items.append(int(item))
    operation = operationLine.split("=")[1]
    test = ifFalseLine.split(" ")[-1] + " if item % " + testLine.split(" ")[-1] + " else " + ifTrueLine.split(" ")[-1]
    testNumber = int(testLine.split(" ")[-1])
    monkeys.append(Monkey(items, operation, test, testNumber))
  return monkeys

def run(monkeys, worryReduction, iterations):
  for _ in range(iterations):
    for monkey in monkeys:
      monkey.inspect(worryReduction)
      monkey.inspectedItems += len(monkey.items)
      for item in monkey.items:
        monkeys[monkey.test(item)].items.append(item)
      monkey.items = []

  mostActiveMonkeys = sorted([monkey.inspectedItems for monkey in monkeys])[-2:]
  return mostActiveMonkeys[0] * mostActiveMonkeys[1]

def part1(monkeys):
  return run(monkeys, lambda x: int(x/3), 20)

def part2(monkeys):
  return run(monkeys, lambda x: x%lcm(*[monkey.testNumber for monkey in monkeys]), 10000)

stringInput = getInput()
print("Part 1: ", part1(getMonkeys(stringInput)))
print("Part 2: ", part2(getMonkeys(stringInput)))