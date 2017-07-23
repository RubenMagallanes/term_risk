from risk_map import Map
from random import randint

class Game(object):
	#risk_map - Map - reference to the map
	#players - list[string] - list of player names
	#message - String - status message 
		#TODO list of player password hashes
		#TODO remove every print string, either set status message or return string
	#TODO state 

	#turn - int - which player's turn it is
	def __init__(self, players, map_fname):
		print 'initializing new game'
		self.players = players	
		self.risk_map = Map(map_fname)
		self.turn = 0
		self.message = ""
		
	def recieve_command(self, cmd):
		'''recieves and processes a command from a player and if it's 
		that player's turn, executes said command assuming it's valid
		TODO take player from to check if can execute
		'''
		print "command string: " + cmd
		parts = cmd.split('-')
		if parts[0] == 'attack':
			#query map check territories exist, ie no typos [1],[2] 
			#are territories

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
		if not self.is_adjacent(t_from, t_to):
			print "territories {} and {} are not adjacent, can't invade"\
				.format(t_from, t_to)
			return
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
		'''
		returns whether attacking from territory 'a_name' with 'army_size' 
		troops into territory 'b_name' is valid.
		attack is valid if both territory names are valid, 1 <= army_size <= 3
		and attacking territory has enough troops.
		'''
		if not self.risk_map.check_territory(a_name):
			self.message = '{} not valid territory'.format(a_name) 
			return False
		if not self.risk_map.check_territory(d_name):
			self.message =  '{} not valid territory'.format(d_name) 
			return False

		if army_size > 3:
			self.message =  'army size larger than 3'
			return False
		
		a_ter = self.risk_map.get_territory(a_name)
		d_ter = self.risk_map.get_territory(d_name)
		army_available = self.risk_map.num_troops_in(a_name)
		army_available -= 1

		if army_available < int(army_size):
			self.message =  'army size {} is more than whats available: {}'\
			.format(army_size, army_available)
			return False

		return True

	def is_adjacent(self, t1_name, t2_name):
		'''
		returns boolean whether territory t1 is adjacent to territory t2 
		'''
		territory1 = self.risk_map.get_territory(t1_name)
		return t2_name in territory1.adjacent

	def roll_dice(self, num):
		'''
		returns an array of num ints with numbers 1-6
		'''
		dice = []
		for i in range (int(num)):
			dice.append(randint(1,6))
		return dice

	def print_game_info(self):
		'''
		returns string info about the game
		'''
		returnstr = ''
		#returnstr += 
		returnstr +=  'printinf info for current {} player game'\
			.format(len(self.players)) + '\n'
		returnstr +=  'players in game:' + '\n'
		for pl in self.players:
			returnstr += '- ' + pl + '\n'
		returnstr +=  'there are {} territories in this map:'\
			.format(len(self.risk_map.territories)) +'\n'
		return returnstr

	def print_map(self):
		"""
		returns a string reprisentation of the map
		"""
		returnstr = ''
		for tr in self.risk_map.territories:
			printstr = tr.name 
			printstr += ': owned by {}'.format(tr.owner)
			printstr += ', {} troops strong'.format(tr.troops)
			printstr += '\n\t - borders: '
			for adj in tr.adjacent:
				printstr += adj + ', '
			returnstr += printstr + '\n'
		return returnstr

	def game_is_won(self):
		'''
		returns string the player that has won the game. if game isn't won 
		yet, returns empty string
		'''
		ownr = self.risk_map.territories[0].owner
		for ter in self.risk_map.territories:
			if ter.owner != ownr:
				return '' # no winner yet
		return ownr # all owners of territories match ownr

