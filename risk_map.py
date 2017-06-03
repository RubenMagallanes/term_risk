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

