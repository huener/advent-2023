def parseLine(line):
	digits = ""
	result = ""
	potentialNumber = ""

	for char in line:
		if str.isdigit(char) is True:
			digits += char
			potentialNumber = ""
		else:
			potentialNumber += char
			numbers = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
			
			for i in range(len(numbers)):
				if numbers[i] in potentialNumber:
					digits += str(i)
					potentialNumber = str(numbers[i])[-1]

		
	if len(digits) == 1:
		digits += digits

	result += digits[0]
	result += digits[-1]
	return str(result)
	
class main():
	file = open("input.txt")
	total = 0

	for line in file:
		if len(line) > 0:
			valueStr = (parseLine(line))
			total += int(valueStr)

	print("Total Value: "+str(total))