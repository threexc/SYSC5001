#!/usr/bin/python3

from random import random
from math import ceil, log

# Solves quesstion 8.15 in Discrete-Event System Simulation, 5th Edition
def generate_geo(mean=2.5, q=0, count=10):

	p_var = 1 / (mean - q + 1)
	results = []

	for i in range(count):
		rnd_val = random()
		p_log = 1 / log(1 - p_var)
		result = ceil(p_log * log(1 - rnd_val) - 1)
		results.append(result)

	print(results)

if __name__ == '__main__':
	generate_geo()
