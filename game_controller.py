from risk_map import Map
from risk_territory import Territory
from risk_game import Game
#controller in mvc	
	
fname = './boards/australia2.board'
rgame = Game(['js', 'rj'], fname)
#populate board with soldiers
t_list = rgame.risk_map.territories
for t in t_list:
	t.troops = 5
t_list[0].owner = 'js'
t_list[1].owner = 'rj'
t_list[2].owner = 'js'
t_list[3].owner = 'rj'



rgame.print_game_info()


# spin asking for commands
while rgame.game_is_won() == '':
	inp = raw_input("\n-\t-\t-\t-\t-\nenter a command, 'h' for help\n>")
	if inp == 'h' or inp == 'help':
		print 'available commands: (i)nfo, (a)ttack, end, (q)uit,'\
		' (t)erritory, (c)ontinent,  (p)layer'
	if inp == 'q' or inp == 'quit':
		break
	if  inp == 'info' or inp == 'i':
		rgame.print_game_info() 
		# TODO change so only access to game is through enter_cmd
	if inp == 'm' or inp == 'map':
		rgame.print_map()
	if inp == 't' or inp == 'territory':
		#get which one
		t_name = raw_input('input name of territory you want info about '\
			"or 'l' for a list of territories\n>")
		if t_name == 'l':
			ts = rgame.risk_map.list_territories()
			pstr = ''
			for tn in ts:
				pstr += tn + ', '
			print pstr
		else:
			if rgame.risk_map.check_territory(t_name):
				t = rgame.risk_map.get_territory(t_name)
				t.print_info()
			else:
				print '{} is not a territory name'.format(t_name)
	if inp == 'p' or inp == 'player':
		pstr = 'players in the game: ' 
		for pl in rgame.players:
			pstr += pl + ', '

		print pstr
		player = raw_input('which player do you want info about?\n>')
		if not player in rgame.players:
			print '{} not a player in this game'.format(player)
		else:
			ters = rgame.risk_map.list_territories()
			string = '{} controls: '.format(player)
			for ter in ters:
				if rgame.risk_map.get_territory(ter).owner == player:
					string += rgame.risk_map\
					.get_territory(ter).name + ', '
			print string

	if inp == 'c' or inp == 'continent':
		print ''
		#list continents, owners, value
		#in depth, list territories in it + info for each

	else:
		#construct cmd to send to model
		if inp == 'attack' or inp == 'a':
			#TODO print list of available territories to attack from to help user
			t_from = raw_input('which territory to attack from?\n>')
			#build list of ones adjacent and owned by other player
			t_to = raw_input('which territory to invade?\n>')
			#again todo, check how many available to attack
			amt = raw_input('with how many troops?\n>')
			cmd_string = 'attack-{}-{}-{}'.format(t_from, t_to, amt)
			result = rgame.recieve_command(cmd_string)
	
#print_map(rgame.risk_map)
