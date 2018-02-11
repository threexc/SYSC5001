import numpy as np
#import matplotlib.pyplot as plt


def eclipse_estimate(x_axis, y_axis, num_trials):
	eclipse_x = np.arange(0., float(x_axis), 0.001)
	x_random = x_axis * np.random.random_sample(num_trials)
	y_random = y_axis * np.random.random_sample(num_trials)
	successes = 0
	probability = 0
	pi_estimate = 0

	#plt.plot(eclipse_x, 2*(1-(eclipse_x/3)**2)**(1/2), 'r--', x_random, y_random, 'bo')
	for i in range(0, num_trials):
		if y_random[i] <= 2*np.sqrt(1-(x_random[i]/3)**2):
			successes = successes + 1

	probability = successes/num_trials
	pi_estimate = 4 * probability

	return successes, probability, pi_estimate
