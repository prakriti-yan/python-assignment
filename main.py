
import sys

class Line:
	def __init__(self, string, number):
		self.string = string
		self.number = number
	
	def __word(self, i):
		return 'Soft' if self.string[i % len(self.string)] == 'S' else 'Tough'

	def __str__(self):
		line = ""
		i = 0
		if (self.number < 0):
			return "Positive integers only!"
		while i < self.number - 2:
			line += self.__word(i) + ', '
			i += 1
		if i == self.number - 2: 
			line += self.__word(i) + ' and '
			i += 1
		if i == self.number - 1:
			word = self.__word(i)
			line += word + '.'
		return line


def print_args(string, numbers):
	for number in numbers:
		print(Line(string, number))

def validation(argv):
	error = False
	if (len(argv) < 2):
		error = True
		return error,
	string = argv[0]
	numbers = []
	if string.count('S') + string.count('T') != len(string):
		error = True
	argv = argv[1:]
	try:
		convert_int = lambda x : int(x)
		numbers = map(convert_int, argv)
		numbers = list(numbers)
	except:
		error = True
	return error, string, numbers

def main(argv):
	result = validation(argv)
	if (result[0]):
		print("Invalid arguments!")
	else:
		print_args(result[1], result[2])


if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print ("Usage: The first argument is a random pattern consisting only of characters S and T. For example 'STTTS'.\n"
			"The following arguments are N (N >= 1) number of integers. For example 1 5 8. Each integer is\n"
			"separated from previous one with a space.")
	else:
		main(sys.argv[1:])
