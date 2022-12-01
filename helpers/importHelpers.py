import sys

def getInput(): #get input from file
  day = sys.argv[0][-4 : -3] #get day number from filename
  with open(f'./inputs/input{day}.txt') as inputFile:
    return inputFile.read().strip()