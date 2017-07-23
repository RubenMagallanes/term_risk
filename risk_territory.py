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

	def lose_troops(self, num):
		self.troops -= num
		if self.troops < 0:
			self.troops = 0

	'''def lose_a_troop(self):
		self.troops -= 1
		if self.troops < 0:
			self.troops = 0
	'''

	def change_owner(self, newplayer):
		self.owner = newplayer

'''
territory helper functions 
'''
		
	def territory_info(territory):
	'''
	return string reprisenting territory info, ready to be printed out
	'''
		return_string = ""
		return_string += 'info for {}:'.format(territory.name)
		return_string += 'owned by {} with {} troops'\
			.format(territory.owner, territory.troops) 
		pstr = 'adjacent territories: '
		for adj in territory.adjacent:
			pstr += adj + ', '
		return_string += pstr
		return return_string
