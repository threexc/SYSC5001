#!/usr/bin/python3

from statistics import mean
from math import sqrt
from random import random

# This class only works under the assumption that the inputs are from question
# 8.4 of Discrete-Event System Simulation, 5th Edition, by Banks. I might make
# it more generalized in the future, including more than one constructor for
# the ability to input b (the mode) instead of the mean

class TriangularGen:

	def __init__(self, a=1, c=10, mean=4):
		self.a = a
		self.c = c

		self.mean = mean
		self.b = 3 * self.mean - self.a - self.c
		self.generated_data = []

	def generate_numbers(self, count):
		for i in range(count):
			rnd_val = random()
			triangular_number = 10 - sqrt(81*(1-rnd_val))
			self.generated_data.append(triangular_number)

	def get_generated(self):
		return self.generated_data

	def get_expectation(self):
		return self.mean
	
	def get_gen_mean(self):
		return mean(self.generated_data)
