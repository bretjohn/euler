#!/usr/bin/python3

# Euler project problem 5
# Author: 	Brett Johnson
# Date:		22 September 2014
# Prompt:
#	Smallest Multiple
#	What is the smallest positive number evenly divisible by 
#	all the numbers from 1 to 20.
#
# Solution:
#	...

import sys
import math

class ThirdProblem:
	def runOld(self, prime = 600851475143):
		prime_sqrt_dbl = math.sqrt(prime)
		prime_sqrt_int = int(prime_sqrt_dbl) + 1
		cur = prime
		factors = []

		for n in range(2,prime_sqrt_int + 1):
			#print("{0}:{1}:{2}".format(cur, n, factors))
			while (True):
				if (cur % n == 0):
					factors.append(n)
					cur = int(cur / n)
				else:
					break
			if (cur == 1 or n > cur):
				break
					
		if (len(factors) == 0):
			factors.append(int(prime))

		return factors

class FifthProblem(ThirdProblem):
	def run(self, end = 20, start = 1):
		factors = []
		tmpFactors = []

		for n in range(start, end, 1):
			newFactors = self.runOld(n)
			tmpFactors = list(factors)
			for w in newFactors:
				if w not in tmpFactors:
					factors.append(w)
				else:
					tmpFactors.remove(w)
		ans = 1
		for n in factors:
			ans *= n

		print("possible ans:{}".format(ans))
		print("factors:{}".format(factors))

		for n in range(start, end, 1):
			if (ans % n != 0):
				print("OHNO!{}".format(n))

		return factors
		

def main(args):
	program = FifthProblem()
	if (len(args) > 1):
		program.run(int(args[1]))
	else:
		program.run()

if __name__ == "__main__":
	main(sys.argv)
