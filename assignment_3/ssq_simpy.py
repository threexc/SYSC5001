# Some sort of approximation to the queue for question 7 of assignment 3


import random as rnd

import simpy

RANDOM_SEED = 42
NEW_CUSTOMERS = 20
ARRIVAL_MEAN = 1.0
SERVICE_MEAN = 0.6


def source(env, number, interval, counter):

	for i in range(number):
		c = customer(env, 'Customer%02d' % i, counter, SERVICE_MEAN)
		env.process(c)
		t = rnd.expovariate(1.0 / interval)
		yield env.timeout(t)

def customer(env, name, counter, service_time):

	arrive = env.now
	print('%7.4f %s: Here I am' % (arrive, name))

	with counter.request() as req:
		results = yield req
		wait = env.now - arrive

		print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))

		servt = rnd.expovariate(1.0 / service_time)
		yield env.timeout(servt)
		print('%7.4f %s: Finished' % (env.now, name))


print('Queue Sim Test')
rnd.seed(RANDOM_SEED)
env = simpy.Environment()

counter = simpy.Resource(env, capacity=1)
env.process(source(env, NEW_CUSTOMERS, ARRIVAL_MEAN, counter))
env.run()
