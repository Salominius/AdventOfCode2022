from helpers.importHelpers import *

class Rock:
  def __init__(self, rockPositions):
    self.rockPositions = rockPositions[:]

  def spawn(self, highestY):
    self.rockPositions[:] = [(x+2,y+highestY+4) for x,y in self.rockPositions] #spawns one position too high, begins falling

  def move(self, direction, ground):
    for rock in self.rockPositions:
      if rock[0] + direction < 0 or rock[0] + direction >= 7:
        return #can't move out of bounds
      if rock[1] in ground[rock[0] + direction]:
        return #can't move in resting blocks
    self.rockPositions[:] = [(x+direction, y) for x,y in self.rockPositions]

  def fall(self, ground):
    for rock in self.rockPositions:
      if rock[1] - 1 in ground[rock[0]]:
        return False #can't fall in ground
    self.rockPositions[:] = [(x,y-1) for x,y in self.rockPositions]
    return True        

def printState(ground, highestY, fallingRock = []): #debugging function, currently unused
  for i in range(highestY, 0, -1):
    print("".join(["#" if i in ground[x] else "@" if (x, i) in fallingRock else "." for x in range(7)]))
  print()

def letThemFall(rockAmount):
  highestY = 0
  ground = [set([0]) for _ in range(7)]
  streamLength = len(jettPattern)
  currentStreamPosition = 0
  
  #Variables for repetition detection:
  highestYList = [0]
  stateList = [0]
  repetitionDetected = False

  i = 0
  while i < rockAmount:
    rock = Rock(rockPatterns[i%5])
    rock.spawn(highestY)
    while True:
      rock.move(jettPattern[currentStreamPosition%streamLength], ground)
      currentStreamPosition += 1
      if not rock.fall(ground):
        break
    for x,y in rock.rockPositions:
      ground[x].add(y)
      if y > highestY:
        highestY = y
    if not repetitionDetected:
      highestYList.append(highestY)
    i+=1

    if not repetitionDetected and i%5 == 0:
      ground = [set(filter(lambda y: y>highestY-100, col)) for col in ground] #cut ground to top 100 elements
      normalizedState = tuple(map(tuple, [set(map(lambda y: y-highestY+100, col)) for col in ground])) #save ground-state in normalized form

      if normalizedState in stateList: #repetition detected when state is already in stateList
        repetitionStart = stateList.index(normalizedState)
        cycleLength = i - repetitionStart
        cycleGain = highestY - highestYList[repetitionStart]
        skippableRepetitions = int((rockAmount-repetitionStart)/cycleLength)-1
        # print("Repetition detected (i: " + str(repetitionStart) + " - " + str(i) + ", length = " +str(cycleLength) + ")")
        # print("skipping", skippableRepetitions, "rounds")
        highestY += skippableRepetitions*cycleGain
        i += skippableRepetitions*cycleLength
        ground = [set(map(lambda y: y+skippableRepetitions*cycleGain, col)) for col in ground]
        repetitionDetected = True
      else:
        stateList.append(normalizedState)
    else:
      stateList.append(0) #fill stateList with dummy values to keep indices in sync
  return highestY

jettPattern = list(map(lambda x: 1 if x == ">" else -1, getInput()))

rockPatterns = []
rockPatterns.append([(0,0), (1,0), (2,0), (3,0)])
rockPatterns.append([(1,0), (0,1), (1,1), (2,1), (1,2)])
rockPatterns.append([(0,0), (1,0), (2,0), (2,1), (2,2)])
rockPatterns.append([(0,0), (0,1), (0,2), (0,3)])
rockPatterns.append([(0,0), (1,0), (0,1), (1,1)])

print("Part 1: ", letThemFall(2022))
print("Part 2: ", letThemFall(1000000000000))