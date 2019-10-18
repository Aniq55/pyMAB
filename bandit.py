import numpy as np

class Bandit:
	def __init__(self, id, p_reward):
		self.id = id
		self.p_reward = p_reward
	
	def get_reward(self):
		return np.random.binomial(1,self.p_reward,1)[0]
