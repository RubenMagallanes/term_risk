from risk_territory import Territory

class Map(object):
	#territories - list[Territory] - list of territory objects
	#continents - list[Continent] - list of continents

	def __init__(self, fname):
		self.territories = []
		self.continents = []

		lines = []
		with open(fname) as f:
			lines = f.read().split('\n')

		t_name = ''
		territory = ''
		for en in lines:
			cmd = en.split(':')
			if cmd[0] == 'c': #continent line
				info = cmd[1].split('-')
				cont = Continent(info[0], info[1], info[2].split(','))
				self.continents.append(cont)
			if cmd[0] == 'n': #territory name
				t_name = cmd[1]
			if cmd[0] == 'a': #adjacent territories + add t
				territory = Territory(t_name, [cmd[1]])
				self.territories.append(territory)

	
	def lose_troop_from(self, ter_name):
		if not self.check_territory(ter_name):
			return
		for t in self.territories:
			if t.name == ter_name:
				t.lose_a_troop()
				break

	def num_troops_in(self, ter_name):
		if not self.check_territory(ter_name):
			return -1
		for t in self.territories:
			if t.name == ter_name:
				return t.troops
			
	def get_territory(self, t_name):	
		for t in self.territories:
			if t.name == t_name:
				return t

	def check_territory(self, name):
		names = []
		for t in self.territories:
			names.append(t.name)
		return name in names
	
	def list_territories(self):
		ts = []
		for t in self.territories:
			ts.append(t.name)
		return ts

