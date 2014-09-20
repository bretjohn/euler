#!/usr/bin/python3

# Euler project problem 1
# Author: 	Brett Johnson
# Date:		17 September 2014
# Prompt:
#	Simple mod sum
#	Find the sum of all multiples of 3 and 5 of ints from 1 to 1000

import sys

class FirstProblem:
	def run(self, start = 1, limit = 1000, mods = [3, 5]):
		finalSum = 0
		#print("BEJ: hi! func:{}".format(sys._getframe().f_code.co_name))
		for x in range(start, limit):
			#print("BEJ:{}".format(x))
			for mod in mods:
				if x % mod == 0:
					finalSum+=x
					break
		print("Final Sum:{}".format(finalSum))

def main():
	program = FirstProblem()
	program.run()

if __name__ == "__main__":
	main()
