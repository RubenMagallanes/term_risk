from risk_territory import Territory
from risk_continent import Continent
class Map(object):
	#territories - list[Territory] - list of territory objects
	#continents - list[Continent] - list of continents

	def __init__(self, fname):
		''' 
		constructs new map object form a file

		a Map keeps a reference & controls access to:
		all the territories in the game
		all the continents in the game
		'''
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
				territory = Territory(t_name, cmd[1].split(','))
				self.territories.append(territory)

'''	territory functions ''' 	
	
	def list_territories(self):
		ts = []
		for t in self.territories:
			ts.append(t.name)
		return ts

	def check_territory(self, t_name):
		''' checks name is a valid territory name '''
		names = []
		for t in self.territories:
			names.append(t.name)
		return t_name in names

	def get_territory(self, t_name):	
		''' returns territory designated by t_name if it exists, otherwise None ''' 
		for t in self.territories:
			if t.name == t_name:
				return t
			else:
				return None

	def lose_troops_from(self, t_name, num_troops):
		if not self.check_territory(t_name):
			return
		ter = self.get_territory(t_name)
		if ter = None: 
			return
		ter.lose_troops(num_troops)

	def add_troops_to(self, t_name, num_troops):
		if not self.check_territory(ter_name):
			return
		for t in self.territories:
			if t.name == t_name:
				t.add_troops(num_troops)
				break

	def num_troops_in(self, ter_name):
		if not self.check_territory(ter_name):
			return 
		for t in self.territories:
			if t.name == ter_name:
				return t.troops

	def path_between(self,  t_from, t_to):
		'''
		calculates the path (if any) between t_from and t_to
		returns True if there exists a path, False if not.
		'''
		#TODO implement graph pathfinding algorithm through
		#same-player owned territorys

	def move_troops(self, t_from, t_to, num_troops):
		'''move num_troops from t_from to t_to'''
		#TODO

'''	continent functions '''

	def list_continents(self):
		cs = []
		for c in self.continents:
			cs.append(c.name)
		return cs

	def check_continent(self, c_name):
		''' checks nc_ame is a valid continent name '''
		names = []
		for c in self.continents:
			names.append(c.name)
		return c_name in names

	def get_continent(self, c_name):
		''' returns continent designated by c_name if it exists, otherwise None ''' 
		for c in continents:
			if c.name == c_name:
				return c
			else:
				return None

	# who owns a continent
	#TODO
	def get_continent_owner(self, c_name):
		''' returns owner of the continent c_name if there is one, empty string if there isnt one '''
		if not check_continent(c_name):
			return "" #empty string if continent doesnt exist
		if not self.get_continent(c_name).isOwned():
			return "" #empty string if continent has no owner
		return self.get_continent(c_name).owner()
			


