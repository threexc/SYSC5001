import numpy as np
import matplotlib.pyplot as plt


def eclipse_plot(x_axis, y_axis, num_trials):
	eclipse_x = np.arange(0., float(x_axis), 0.001)
	x_random = x_axis * np.random.random_sample(num_trials)
	y_random = y_axis * np.random.random_sample(num_trials)

	#plt.plot(eclipse_x, 2*(1-(eclipse_x/3)**2)**(1/2), 'r--', x_random, y_random, 'bo')
	plt.plot(x_random, y_random, 'bo')
	plt.fill_between(eclipse_x, 2*np.sqrt(1-(eclipse_x/3)**2), 0, color = '0.7')
	plt.xlim(xmin = 0)
	plt.ylim(ymin = 0)
	plt.show()
