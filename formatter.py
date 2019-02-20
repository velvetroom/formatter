import sys
import os

def format(directory):
	printed = False
	for r, d, n in os.walk(directory):
		for i in n:
			if i.endswith(".swift"):
				print(r + "/" + i)
				printed = True
				fp = open(r + "/" + i)
				for l in fp.read().split(":"):
					print(l)
					break
# 					if len(l) > 0: 
# 						print(len(1))
# 					print("\n")
				fp.close()
				break
		if printed:
			break

if __name__ == '__main__':
	format(sys.argv[1])

def fibonacci(num):
	return num + 1
