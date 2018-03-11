# DataSet is a class used to evaluate certain statistical properties, such as
# uniformity, independence, goodness-of-fit of data sets as part of the class
# SYSC5001 at Carleton University, Winter 2018

from scipy.stats import chisquare
from math import ceil, floor

class DataSet:
	def __init__(self, filename):
		self.data = []

		with open(filename) as f:
			for line in f:
				self.data.append(float(line.strip('\n').replace('"','')))
		f.close()

		self.count = len(self.data)
		self.D_plus_values = [0]*self.count
		self.D_minus_values = [0]*self.count
		self.D_value = None
		self.autocorrelation_value = None

	def set_uniformity_value(self):

		for i in range(0,self.count):
			self.D_plus_values[i] = (i+1) / self.count - self.data[i]
			self.D_minus_values[i] = self.data[i] - i / self.count

		D_plus = max(self.D_plus_values)
		D_minus = max(self.D_minus_values)
		self.D_value = max(D_plus, D_minus)

	def get_uniformity_value(self):
		return self.D_value

	# Runs an autocorrelation calculation on the every step_length numbers in
	# the data set, starting with the value start_point. Note that this function
	# assumes that the data set is counted beginning at 0
	def set_independence_value(self, start_point, step_length):

		M_value = floor(((self.count - start_point) / step_length) - 1)
		autocor_sum = 0

		for k in range(0,M_value):
			autocor_sum = autocor_sum + self.data[start_point + k * step_length] * self.data[start_point + (k + 1) * step_length]
		autocor_sum = autocor_sum - 0.25
		self.autocorrelation_value = autocor_sum / (M_value + 1)

	def get_independence_value(self):
		return self.autocorrelation_value
