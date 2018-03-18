#!/usr/bin/python3

# test_uniformity calculates the max D value for evaluating data sets with the
# Kolmogorov-Smirnov test
def test_uniformity(filename):

	data = []
	D_plus_values = []
	D_minus_values = []

	count = 0

	with open(filename) as f:
		for line in f:
			data.append(float(line.strip('\n').replace('"','')))
	f.close()

	count = len(data)
	D_plus_values = [0]*count
	D_minus_values = [0]*count

	for i in range(0,count):
		D_plus_values[i] = (i+1)/count - data[i]
		D_minus_values[i] = data[i] - i/count

	D_plus = max(D_plus_values)
	D_minus = max(D_minus_values)
	D_value = max(D_plus, D_minus)

	return D_value

if __name__ == '__main__':
	print("The D value for this set is: " + str(test_uniformity("7_20_data")) + "\n")
