from math import log
import numpy as np
import random as rnd
import queue as qu

# This class exists to provide exponentially-distributed packets to the queue
class ExpPacket:

	def __init__(self, interarrival_mean, service_mean, current_time):
		arrival_rnd = rnd.random()
		service_rnd = rnd.random()
		self.inter_mean = interarrival_mean
		self.serv_mean = service_mean
		self.arrival_time = current_time + (-1) * log(arrival_rnd) / self.inter_mean
		self.service_time = (-1) * log(service_rnd) / self.serv_mean
		self.serv_start = 0

	def arrival_time(self):
		return self.arrival_time

	def service_time(self):
		return self.service_time

''' This class creates tuples for the event list of the queue. Not used
class QueueEvent:

	def __init__(self, packet, event_type="ARRIVAL"):
		self.packet = packet
		self.event_type = event_type

	def get_type(self):
		return self.event_type


	def process_event(self):
		processed = {self.time, self.packet, self.event_type}
		return processed
'''

class ExpSSQ:

	# This particular SSQueue class depends on the type of packet passed to it
	# to determine the arrival and service distributions. Since it is assumed
	# that the arrival queue may be infinite, note that queue_size defaults to
	# -1 to set the self.arrival_queue object to be of infinite size, as per
	# the Queue documentation.
	def __init__(self, arrival_mean, service_mean, arrival_size=-1, server_size=1):

		self.arrival_mean = arrival_mean
		self.service_mean = service_mean
		self.arrival_queue = qu.queue(arrival_size)
		self.server_queue = qu.queue(server_size)

		self.arrival_times = []
		self.departure_times= []
		self.event_list = []
		self.occupancy_count = []

		# Set both self.time and self.next_event_time equal to 0, where the
		# 0-time "event" will correspond to initialization of the system
		self.time = 0

	# the event method only schedules events, it does not process the queue
	def event(self, packet, event_type):

		# event method doesn't care what type the event actually is if the time
		# is 0 (the initial state is being set)
		if self.time == 0:

			# Generate the first packet, but do not put it on the arrival queue
			# until its arrival time
			packet = ExpPacket(self.arrival_mean, self.service_mean, self.time)
			event_time = self.time + packet.arrival_time()
			the_event = {packet, event_time, "FIRST ARRIVAL"}
			self.event_list.append(the_event)

		else if event_type == "ARRIVAL":

			packet = ExpPacket(self.arrival_mean, self.service_mean, self.time)
			arrival_time = self.time + packet.arrival_time()
			arrival_event = {packet, arrival_time, "ARRIVAL"}
			self.event_list.append(arrival_event)

			if self.server_queue.empty():
				departure_time = arrival_time + packet.service_time()
				depart_event = {packet, departure_time, "DEPARTURE"}
				self.event_list.append(depart_event)

		else if event_type == "DEPARTURE":

	# count here corresponds to the number of events to simulate
	def simulate_system(self, count):

		for iteration in range(0, count):

			packet = ExpPacket(arrival_mean, service_mean, self.time)

			if self.time == 0:
				event = {packet, packet.arrival_time()}
				arrival_times.append(event)
			else
