from risk_map import Map
from random import randint

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
			#query map check territories exist, ie no typos [1],[2] are territories
			t1 = self.risk_map.check_territory(parts[1])
			t2 = self.risk_map.check_territory(parts[2])
			if t1 and t2:
				self.attack(parts[1], parts[2], parts[3])
			else:
				print "couldn't attack, possibly a typo in territory names?" 
	#TODO make print statements return string`

	def attack(self, t_from, t_to, army_size):
		#validate inputs
		valid = self.validate_attack_input(t_from, t_to, army_size)
		if not valid:
			return
		#check territory is neighbour

		#generate attackers dice
		a_dice = self.roll_dice(army_size)
		#generate defenders dice
		defs = self.risk_map.num_troops_in(t_to)
		if defs == -1:
			print 'invalid defending territory name'
			return
		d_dice = []
		if defs == 1:
			d_dice = self.roll_dice(1)
		else:
			d_dice = self.roll_dice(2)
		
		#print dice
		printstr = '{} rolls: '.format(t_from)
		for roll in a_dice:
			printstr +=  str(roll)+ ' '
		print printstr
		printstr = '{} rolls: '.format(t_to)
		for roll in d_dice:
			printstr += str(roll) + ' '
		print printstr

		#sort then reverse each dice list so it's highest -> lowest
		a_dice.sort()
		a_dice.reverse()
		d_dice.sort()
		d_dice.reverse()
		
		#calculate smallest dice array size
		smallest = 3
		if len(a_dice) < smallest:
			smallest = len(a_dice)
		if len(d_dice) < smallest:
			smallest = len(d_dice)

		#calculate casuaties
		for dice in range(smallest):
			if a_dice[dice] > d_dice[dice]:
				print '{} wins a roll, {} suffers a casualty'\
					.format(t_from, t_to)
				self.risk_map.lose_troop_from(t_to)
			else:
				print '{} wins a roll, {} suffers a casualty'\
					.format(t_to, t_from)
				self.risk_map.lose_troop_from(t_from)
		#battle over

	def validate_attack_input(self, a_name, d_name, army_size):
		if not self.risk_map.check_territory(a_name):
			print '{} not valid territory'.format(a_name) 
			return False
		if not self.risk_map.check_territory(d_name):
			print '{} not valid territory'.format(d_name) 
			return False
		
		a_ter = self.risk_map.get_territory(a_name)
		d_ter = self.risk_map.get_territory(d_name)
		army_available = self.risk_map.num_troops_in(a_name)
		army_available -= 1
		if army_available < int(army_size):
			print 'army size {} is more than whats available: {}'\
			.format(army_size, army_available)
			return False

		return True
	
	def roll_dice(self, num):
		'''returns an array of num ints with numbers 1-6
		'''
		dice = []
		for i in range (int(num)):
			dice.append(randint(1,6))
		return dice

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
	def print_map(self):
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

