from risk_territory import Territory

class Map(object):
	#territories - list of territory objects
	
	def __init__(self, fname):
		self.territories = []
		#self.continents = [] TODO
		
		lines = []
		with open(fname) as f:
			lines = f.read().split('\n')

		t_name = ''
		territory = ''
		for en in lines:
			cmd = en.split(':')
			if cmd[0] == 'n':
				t_name = cmd[1]
			if cmd[0] == 'a':
				territory = Territory(t_name, [cmd[1]])
				self.territories.append(territory)
	
	def lose_troop_from(self, ter_name):
		if not check_territory(name):
			return
		for t in self.territories:
			if t.name == ter_name:
				t.lose_a_troop()
				break

	def num_troops_in(self, ter_name):
		if not check_territory(name):
			return -1
		for t in self.territories:
			if t.name == ter_name:
				return t.troops
				


	def check_territory(self, name):
		names = []
		for t in self.territories:
			names.append(t.name)
		return name in names

