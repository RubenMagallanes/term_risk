from risk_map import Map

class Game(object):
	#risk_map - Map - reference to the map
	#players - list[string] - list of player names
	#TODO list of player password hashes

	#TODO state 

	#turn - int - which player's turn it is
	def __init__(self, players, map_fname):
		print 'initializing new game'
		self.players = players	
		self.risk_map = Map(map_fname)
		self.turn = 0
		
	def recieve_command(self, cmd):
		'''recieves and processes a command from a player and if it's 
		that player's turn, executes said command assuming it's valid
		TODO take player from to check if can execute
		'''
		print "command string: " + cmd
		parts = cmd.split('-')
		if parts[0] == 'attack':
			self.attack(parts[1], parts[2], parts[3])
	
	def attack(self, t_from, t_to, army_size):
		#implement attacking lul
		print 'attacking with {} soldiers from {} to {},'\
			' yet to be implemented'.format(army_size, t_from, t_to )
	def print_game_info(self):
		print 'printinf info for current {} player game'.format(len(self.players))
		print 'players in game:'
		for pl in self.players:
			print '- ' + pl
		print 'there are {} territories in this map:'.format(len(self.risk_map.territories))
		for tr in self.risk_map.territories:
			printstr = tr.name 
			printstr += ', owned by {}'.format(tr.owner)
			printstr += ', {} troops strong'.format(tr.troops)
			printstr += '\n\t - borders: '
			for adj in tr.adjacent:
				printstr += adj + ', '
			print printstr
	
	def game_is_won(self):
		'''
		returns the player that has won the game. if game isn't won 
		yet, returns empty string
		'''
		ownr = self.risk_map.territories[0].owner
		for ter in self.risk_map.territories:
			if ter.owner != ownr:
				return '' # no winner yet
		return ownr # all owners of territories match ownr

