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
	inp = raw_input("enter a command, 'h' for help:\n>")
	if inp == 'h' or inp == 'help':
		print 'available commands: info, attack, end'
	if inp == 'game info' or inp == 'info' or inp == 'i':
		rgame.print_game_info() 
		# TODO change so only access to game is through enter_cmd
	if inp == 'm' or inp == 'map':
		rgame.print_map()
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
