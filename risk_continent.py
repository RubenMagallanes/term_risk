class Continent(object):
	#name - string - name of this continent
	#value - int - bonus for controlling this continent at start of turn
	#territories - [str] - territories that make up this continent
	def __init__(self, cname, cvalue, t_list):
		self.name = cname
		self.value = cvalue
		self.territories = t_list
	
	def territory_list(self):
		return territories

