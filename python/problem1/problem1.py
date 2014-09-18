#!/usr/bin/python3
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
