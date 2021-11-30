file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

def parse(x, id):
	try:
		return int(x)
	except:
		return reg[id][x]

reg = [{}, {}]

for instr in l:
	name = instr.split()[1]

	if name not in reg[0].keys() and not name.isdecimal():
		for id in range(2):
			reg[id].update({name: int(name == "p" and id == 1)})

count = 0

ip = [0, 0]
queue = [[], []]
blocked = [False, False]
id = 0
while not blocked[0] or not blocked[1]:
	if ip[id] < 0 or ip[id] > len(l)-1:
		blocked[id] = True
		id = 1 - id
		continue

	command, *args = l[ip[id]].split()

	if command == "snd":
		queue[1-id].append(parse(args[0], id))

		if ip[1-id] > -1 and ip[1-id] < len(l):
			blocked[1-id] = False

		if id == 1:
			count += 1
	elif command == "set":
		reg[id].update({args[0]: parse(args[1], id)})
	elif command == "add":
		reg[id].update({args[0]: reg[id][args[0]] + parse(args[1], id)})
	elif command == "mul":
		reg[id].update({args[0]: reg[id][args[0]] * parse(args[1], id)})
	elif command == "mod":
		reg[id].update({args[0]: reg[id][args[0]] % parse(args[1], id)})
	elif command == "rcv":
		if not queue[id]:
			blocked[id] = True
			id = 1 - id
			continue
		value = queue[id].pop(0)
		reg[id].update({args[0]: value})
	elif command == "jgz":
		if parse(args[0], id) > 0:
			ip[id] += parse(args[1], id)
			continue
	
	ip[id] += 1

print(count)