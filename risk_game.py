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

	def attack(self, t_from, t_to, army_size):
		#TODO make print statements return string
		if army_size > 3:
			army_size = 3
		print 'attacking with {} soldiers from {} to {},'.format(army_size, t_from, t_to )
		#calculate dice rolls
		#calculate attacker has enough to attack with
		available = self.risk_map.num_troops_in(t_from)
		available -= 1	#ones gotta stay behind in territory
		atk_with = 0
		#make sure theyre not trying to attack with more than they have
		if army_size > available:  #if trying to atk with more 
			atk_with = available #attack with what they have 
		else:
			atk_with = army_size
		if atk_with == 0:
			print 'no troops to attack with'
			return
		a_dice = self.roll_dice(atk_with)
		d_dice = []
		if self.risk_map.num_troops_in(t_to) == 1:
			d_dice = self.roll_dice(1)
		else:
			d_dice = self.roll_dice(2)
		#print dice rolls
		print 'attacker rolls: '
		for i in a_dice:
			if i != 0:
				print str(i) + ' '
		print '\ndefender rolls: '
		for i in d_dice:
			if i != 0:
				print str(i) + ' '
		#sort lists
		a_dice.sort()
		a_dice.reverse()
		d_dice.sort()
		d_dice.reverse()
		#calculate casuaties
		for dice in range(3):
			if a_dice[dice] == 0 or d_dice[dice] == 0:
				continue
			if a_dice[dice] > d_dice[dice]:
				self.risk_map.lose_troop_from(t_to)
			else:
				self.risk_map.lose_troop_from(t_from)
		print 'fight over'

	def roll_dice(self, num):
		'''returns an array of 3 ints with num numbers of 1-6, rest 0
		'''
		dice = []
		for i in range (3):
			if i < num:
				dice.append(randint(1,6))
			else:
				dice.append(0)
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

