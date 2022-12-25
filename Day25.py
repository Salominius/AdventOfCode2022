from helpers.importHelpers import *

getDecimal = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

def getRequiredFuel(stringInput):
  requiredFuel = 0
  for line in stringInput.split("\n"):
    for rank, digit in enumerate(line[-1::-1]): # itereate from right to left through every line
      requiredFuel += getDecimal[digit] * 5**rank # add the value of each digit*rankValue to the total fuel
  return requiredFuel

def convertToSnafu(number):
  result = []
  while number > 0:
    number += 2 # if the number is increased by 2 at every rank, we can later subtract 2 from each digit to get the SNAFU-notation
    result.insert(0, number % 5) # insert smallest rank digit of current number in front of list
    number = number // 5 # get rid of the smallest rank digit (// is floor division) (just as //10 removes smallest rank digit for base 10)
  return "".join(map(lambda x: "=-012"[x], result)) # subtracts 2 from each digit and converts to SNAFU-notation

print("Part 1: ", convertToSnafu(getRequiredFuel(getInput())))
print("Part 2: ", 0)