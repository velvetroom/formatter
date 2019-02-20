import sys
import os

def format(directory):
	for r, d, f in os.walk(directory):
		for file in f:
			if file.endswith(".swift"):
				print(file)

if __name__ == '__main__':
	format(sys.argv[1])


def fibonacci(num):
	return num + 1
