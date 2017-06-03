from risk_map import Map
from risk_territory import Territory

fname = './australia.board'
def generate_map_from_file(filename):
	map_to_ret = Map()

	li1 = []
	with open(filename) as f:
		li1 = f.read().split('\n')
			
	t_name = ''
	territory = ''
	for en in li1:
		cmd = en.split(':')
		if cmd[0] == 'n':
			t_name = cmd[1]
		if cmd[0] == 'a':
			territory = Territory(t_name, [cmd[1]])
			if territory != '':
				map_to_ret.add_territory(territory)

	return map_to_ret

risk = generate_map_from_file(fname)

for i in risk.territories:
	printstr = i.name + " - borders: ["
	for j in i.adjacent:
		printstr += j + ", "
	printstr += ']'
	print printstr
