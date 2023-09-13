from random import choice
import sys


def decide(filename="options.txt"):
	with open(filename, "r") as file:
		options = file.readlines()

	random_option = choice(options)

	print(random_option)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename=sys.argv[1]
	else:
		filename="options.txt"
		
	decide(filename)
