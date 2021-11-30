file = open("aoc13_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

def get_max_happiness(in_circle, available):
	in_circle = [j for j in in_circle]
	happiness = 0

	if len(in_circle) == len(available):
		for i in range(len(in_circle)):
			happiness += d[in_circle[i]][in_circle[(i+1)%len(in_circle)]] + d[in_circle[(i+1)%len(in_circle)]][in_circle[i]]
		return happiness
	
	for i in available:
		if i not in in_circle:
			happiness = max(happiness, get_max_happiness(in_circle + [i], available))
	
	return happiness

d = dict()

for i in l:
	s = i[:-1].replace("would gain ", "").replace("would lose ", "-").replace(" happiness units by sitting next to", "").split()
	
	if s[0] not in d.keys():
		d.setdefault(s[0], dict())
	if s[2] not in d.keys():
		d.setdefault(s[2], dict())

	d[s[0]].setdefault(s[2], int(s[1]))

print(get_max_happiness([], d.keys()))