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
		#self.turn = 0
		#self.message = ""
		
	''' helper functions for attacking ''' 

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
	''' TODO validate attack input in gamecontroller ''' 

	''' now the attack function ''' 
	def attack(self, t_from, t_to, army_size):
		''' 
		attacks from t_from to t_to with army_size troops. 
		1<= army_size <= 3
		assumes move is valid

		returns True if attack has wiped out defending army 
				False if defending territory still contains troops
		'''
		#generate both attackers & defenders dice
		a_dice = self.roll_dice(army_size)
		defs = self.risk_map.num_troops_in(t_to)
		d_dice = []
		if defs == 1:
			d_dice = self.roll_dice(1)
		else:
			d_dice = self.roll_dice(2)

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
				self.risk_map.lose_troop_from(t_to)
			else:
				self.risk_map.lose_troop_from(t_from)

		#TODO if defending territory ends up with 0 troops, move 1 attacker in, 
		#return True indicating attacker should be prompted to choose how 
		#many troops to move from t_from to t_to
		#
		#battle over
		return False

	''' other functions ''' 
	def move_troops(self, t_from, t_to, num_troops):
		''' 
		moves num-troops from t_from to t_to. 
		both must be owned by the same player and must have a path 
		of connecting territorys 
		'''
		#TODO pathfinding algorithm from t_from , through same-player
		#owned territories to t_to

		return

	def game_winner(self):
		'''
		returns string the player that has won the game. if game isn't won 
		yet, returns empty string
		'''
		ownr = self.risk_map.territories[0].owner
		for ter in self.risk_map.territories:
			if ter.owner != ownr:
				return '' # no winner yet
		return ownr # all owners of territories match ownr

