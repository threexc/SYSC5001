from eclipse_estimate import *
import numpy as np
import matplotlib.pyplot as plt

def eclipse_table(x_length, y_length, num_trials):
	values = []
	#successes = []
	lower_bound = []
	upper_bound = []

	x = np.arange(0,num_trials)
	ones = np.ones(num_trials)
	for i in range(1, num_trials+1):
		result = eclipse_estimate(x_length, y_length, i)
		#successes.append(result[0])
		values.append(result[1])

	#lower_bound = np.subtract(values, 1.96*np.sqrt(values*(ones - values)/num_trials))
	#upper_bound = np.add(values, 1.96*np.sqrt(values*(ones - values)/num_trials))
	lower_bound = values - 1.96*np.sqrt(values*(ones - values)/num_trials)
	upper_bound = values + 1.96*np.sqrt(values*(ones - values)/num_trials)
	#plt.plot(x, values)
	#plt.fill_between(x, lower_bound, upper_bound, color = '0.7')
	#plt.show()

	table_values = []
	for j in range(100, 2100, 100):
		t = j, values[j], lower_bound[j], upper_bound[j]
		table_values.append(t)
