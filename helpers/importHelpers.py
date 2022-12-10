import sys

def getInput(noStrip = False): #get input from file
  fileName = sys.argv[0] #get filename
  if fileName[-5: -3].isdigit(): #check if day number is 2 digits long (ugly solution for now)
    day = fileName[-5: -3] #get day number from filename
  else:
    day = fileName[-4: -3] #get day number from filename  
  with open(f'./inputs/input{day}.txt') as inputFile:
    return inputFile.read() if noStrip else inputFile.read().strip()