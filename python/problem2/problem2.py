#!/usr/bin/python3

# Euler project problem 2
# Author: 	Brett Johnson
# Date:		18 September 2014
# Prompt:
#	Fibonacci sequence.
#	Find the sum of even-valued terms up to four million

import sys

class SecondProblem:
	def run(self, start = [1,1], limit = 4000000, mods=[2,]):
		finalSum = 0
		fullSum = 0
		prev = start[0]
		cur = start[1]
		tmp = cur
		#print("BEJ: hi! func:{}".format(sys._getframe().f_code.co_name))
		while cur < limit:
			print("BEJ:{0}:{1}".format(prev, cur))
			tmp = cur + prev
			prev = cur
			cur = tmp

			fullSum += cur
			for mod in mods:
				if cur % mod == 0:
					finalSum += cur
					break

		print("Final Sum:{0}, Full Sum:{1}".format(finalSum,
			fullSum))

def main():
	program = SecondProblem()
	program.run()

if __name__ == "__main__":
	main()
