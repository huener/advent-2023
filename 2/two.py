redTotal = 12
greenTotal = 13
blueTotal = 14

def rmSemicolon(cubes):
	for i in range(len(cubes)):
		if "; " in cubes[i]:
			entry = cubes.pop(i)
			split = entry.split("; ")
			for x in range(len(split)):
				cubes.append(split[x])
			i -= 1
		for i in range(len(cubes)):
			if "; " in cubes[i]:
				entry = cubes.pop(i)
				split = entry.partition("; ")
				cubes.append(split[0])
				cubes.append(split[2])
				i -= 1
		for i in range(len(cubes)):
			if "; " in cubes[i]:
				entry = cubes.pop(i)
				split = entry.partition("; ")
				cubes.append(split[0])
				cubes.append(split[2])
				i -= 1
	return cubes
	
def testGamePotential(cubes):
	isPossible = True
	
	for entry in cubes:
		(number, delim, color) = entry.partition(" ")
		if color == "red":
			if(redTotal < int(number)):
				isPossible = False
		elif color == "blue":
			if(blueTotal < int(number)):
				isPossible = False
		elif color == "green":
			if(greenTotal < int(number)):
				isPossible = False
	return isPossible

def testGamePowers(cubes):
	redMin = -1
	blueMin = -1
	greenMin = -1

	for entry in cubes:
		(number, delim, color) = entry.partition(" ")
		number = int(number)
		if color == "red":
			if redMin == -1:
				redMin = number
			elif (redMin < number):
				redMin = number
		elif color == "blue":
			if blueMin == -1:
				blueMin = number
			elif (blueMin < number):
				blueMin = number
		elif color == "green":
			if greenMin == -1:
				greenMin = number
			elif (greenMin < number):
				greenMin = number

	if redMin == -1:
		redMin = 0
	if blueMin == -1:
		blueMin = 0
	if greenMin == -1:
		greenMin = 0
	
	return redMin * blueMin * greenMin
	
class main():
	file = open("input.txt")
	sumID = 0
	sumPower = 0

	for line in file:
		# parse game line into game ID and array of strings in form (# color)
		(game, delim, cubeString) = line.partition(": ")
		cubesString = cubeString.partition("\n")[0]
		game = game.partition(" ")[2]
		cubes = cubesString.split(", ")
		cubes = rmSemicolon(cubes)

		# Part One
		isPossible = testGamePotential(cubes)

		print(game, isPossible, cubes)
		if(testGamePotential(cubes)):
			sumID += int(game)

		# Part Two
		gamePower = testGamePowers(cubes)
		sumPower += gamePower
		print("power:", gamePower, "\n")

	
	print("ID sum (part 1):", sumID)
	print("Power sum (part 2):", sumPower)
		

	