class Territory(object):
	#name - string - territory name
	#adjacent - list[string] - list of other territory names
	
	#owner - string - name of player owns this territory
	#troops - int - number of troops in this territory

	def __init__(self, tname, next2):
		self.name = tname
		self.adjacent = next2
		self.owner = "" # starts empty
		self.troops = 0

	def add_troops(self, num):
		self.troops += num

	def remove_troops(self, num):
		self.troops -= num

	def lose_a_troop(self):
		self.troops -= 1
		if self.troops < 0:
			self.troops = 0

	def change_ownership(self, newplayer):
		self.owner = newplayer

