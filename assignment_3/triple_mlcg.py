

class TripleMultiGen:

	# Initialize with default numeric inputs as specified in problem 7.16 of
	# Discrete-Event System Simulation by J.Banks, J.S. Carlson, Fifth Edition,
	# provided no other values are given.
	def __init__(self, multipliers=[157,146,142], moduli=[32363,31727,31657]):
		self.multipliers = multipliers
		self.moduli = moduli

		# The W's represent the individual multiplicative generators and the
		# values that they each generate. See L'Ecuyer [1988] for more info
		
		self.W_one = []
		self.W_two = []
		self.W_three = []

		self.d = self.moduli[0] - 1
		self.numbers = []

	def generate_numbers(self, count, seeds=[100,300,500]):

		for i in range(0, count):
			if i == 0:
				self.W_one.append(self.multipliers[0]*seeds[0] % self.moduli[0])
				self.W_two.append(self.multipliers[1]*seeds[1] % self.moduli[1])
				self.W_three.append(self.multipliers[2]*seeds[2] % self.moduli[2])
			else:
				self.W_one.append(self.multipliers[0]*self.W_one[i-1] % self.moduli[0])
				self.W_two.append(self.multipliers[1]*self.W_two[i-1] % self.moduli[1])
				self.W_three.append(self.multipliers[2]*self.W_three[i-1] % self.moduli[2])
			self.numbers.append((self.W_one[i] + self.W_two[i] + self.W_three[i]) % self.d)

	def get_generated_numbers(self):
		return self.numbers
