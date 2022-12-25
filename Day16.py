from helpers.importHelpers import *
import re

valves = {} # {name: (flowRate, neighbours), ...}
for line in getInput().split("\n"):
  name, flowRate, *neighbours = re.findall(r"(\d+|[A-Z]{2})", line)
  valves[name] = (int(flowRate), neighbours)

def part1():
  paths = [(0, "AA", [])] # [(currentValue, currentValve, openValves), ...]
  remainingMinutes = 30

  while remainingMinutes > 0:
    newPaths = []
    for path in paths:
      releasedPressure, currentValve, openValves = path
      for neighbour in valves[currentValve][1]:
        newPaths.append((releasedPressure, neighbour, openValves))
      if currentValve not in openValves and currentValve[0] != 0:
        # open valve
        releasedPressure += valves[currentValve][0]*(remainingMinutes-1)
        newPaths.append((releasedPressure, currentValve, openValves + [currentValve]))
    paths = sorted(newPaths, key=lambda x: x[0], reverse=True)[:1000] # only keep the 1000 "best" paths
    remainingMinutes -= 1
  return max(paths, key=lambda x: x[0])[0]

print("Part 1: ", part1())
print("Part 2: ", 0)