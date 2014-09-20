#!/usr/bin/python3

# Euler project problem 2
# Author: 	Brett Johnson
# Date:		19 September 2014
# Prompt:
#	Prime factors
#	Find the largest prime factor of 600851475143
#
# Solution:
#	Kind of a stupid approach, basically try every number up
#	to the celing of the sqrt of the prime (since none above it),
#	or we have found all the primes.

import sys
import math

class ThirdProblem:
	def run(self, prime = 600851475143):
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
		print("Your Factors are {}".format(factors))

def main(args):
	program = ThirdProblem()
	if (len(args) > 1):
		program.run(float(args[1]))
	else:
		program.run()

if __name__ == "__main__":
	main(sys.argv)
