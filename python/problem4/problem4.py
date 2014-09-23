#!/usr/bin/python3

# Euler project problem 3
# Author: 	Brett Johnson
# Date:		22 September 2014
# Prompt:
#	Palendrome Products
#
#	Find the largest palendrome product that is a
#	product of two three digit numbers.
#
# Solution:
#	Start with the max and the min of what we could
#	have with 3 digits. Then starting with the max, try to mod
#	by all the possible 3 digit ints we could have, when we find
#	mod == 0, check if it is also three digits. That is the answer.

import sys
import math

class FourthProblem:
	def isPalendrome(self, num):
		numStr = str(num)
		stack = []
		for c in numStr:
			stack.append(c)
		for d in numStr:
			e = stack.pop()
			if (e != d):
				return False
		return True

	def run(self):
		factor1 = 0
		factor2 = 0
		palendrome = 0
		threeDigitMin = 100
		threeDigitMax = 999
		valueMin = threeDigitMin * threeDigitMin
		valueMax = threeDigitMax * threeDigitMax

		for n in range(valueMax, valueMin, -1):
			if (self.isPalendrome(n)):
				for x in range(threeDigitMax, threeDigitMin, -1):
					if (n % x == 0 and int(n/x) < threeDigitMax):
						palendrome = n
						factor1=x
						factor2=int(n/x)
						break
			if (factor1 != 0 and factor2 != 0):
				break

		print("Your Factors are {}={}*{}".format(palendrome,factor1, factor2))

def main(args):
	program = FourthProblem()
	program.run()

if __name__ == "__main__":
	main(sys.argv)
