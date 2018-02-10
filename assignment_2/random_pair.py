import random as r

def random_pair(low_1, high_1, low_2, high_2):
	result = r.uniform(low_1, high_1), r.uniform(low_2, high_2)
	return result
