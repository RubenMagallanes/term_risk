class Map(object):
	#territories - list of territory objects
	
	def __init__(self):
		self.territories = []
		#self.continents = [] TODO
	
	def add_territory(self, territory):
		self.territories.append(territory)


