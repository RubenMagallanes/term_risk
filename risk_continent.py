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

	def continent_info(self):
		return_string = ''
		return_string += '{} : {}\n'.format(name, value)
		return_string += 'TODO: add who controls this\n'
		return_string += 'territories in {}: '.format(name)
		for t in self.territory_list():
			return_string += t.name
		return return_string

	def is_owned(self):
		'''returns weather thi sis owned by just one person or not'''
		#all territories' owner must match the owner of the first, compare
		t1_owner = self.territories[0].owner
		for t in self.territories;
			if t.owner != t1_owner:
				return False
		return True

	def owner(self):
		'''calculates the owner '''
		if self.is_owned():
			return self.territories[0].owner
		return 'nobody'
