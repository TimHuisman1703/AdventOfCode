import re

file = open("aoc11_input.txt")
l = file.read().split("\n")
file.close()

elements = []
floor = [[] for j in range(4)]
y = 0

for i in range(4):
	content = l[i][20 + [5, 6, 5, 6][i]:-1]
	contents = re.split(", and |, ", content)
	
	if contents == ["nothing relevant"]:
		continue

	for obj in contents:
		kind = obj.split()[1]

		if "-" in kind:
			floor[i].append("chip-" + kind.split("-")[0])
		else:
			elements.append(kind)
			floor[i].append("gen-" + kind)

floor[0] += ["gen-elerium", "chip-elerium", "gen-dilithium", "chip-dilithium"]

states_been_in = set()
states_been_in.add(f"{y}, {[sorted(f) for f in floor]}")

queue = [[0, y, floor.copy()]]

def is_new_and_safe(y, floor):
	global states_been_in

	state = f"{y}, {[sorted(f) for f in floor]}"
	if state in states_been_in:
		return False

	for f in floor:
		for obj in f:
			if obj.startswith("gen"):
				break
		else:
			continue

		for obj in f:
			if obj.startswith("chip"):
				if "gen-" + obj[5:] not in f:
					return False
	
	states_been_in.add(state)

	return True

max_cost_found = 0
while True:
	cost, y, floor = queue.pop(0)
	
	if cost > max_cost_found:
		max_cost_found = cost
		print(cost)

	for i in range(3):
		if floor[i]:
			break
	else:
		print("Result:", cost)
		break

	possible_moves = []
	possible_carry = []

	objects_on_floor = floor[y]
	for i in range(len(objects_on_floor)):
		for j in range(i, len(objects_on_floor)):
			if i == j:
				possible_carry.append([objects_on_floor[i]])
			else:
				possible_carry.append([objects_on_floor[i], objects_on_floor[j]])
	
	if y < 3:
		for carry in possible_carry:
			new_floor = [[j for j in floor[i]] for i in range(4)]

			for c in carry:
				new_floor[y].remove(c)
				new_floor[y+1].append(c)
			
			possible_moves.append([cost+1, y+1, new_floor])
	if y > 0:
		for carry in possible_carry:
			new_floor = [[j for j in floor[i]] for i in range(4)]

			for c in carry:
				new_floor[y].remove(c)
				new_floor[y-1].append(c)
			
			possible_moves.append([cost+1, y-1, new_floor])
	
	good_moves = []
	for move in possible_moves:
		if is_new_and_safe(move[1], move[2]):
			good_moves.append(move)

	for move in good_moves:
		queue.append(move)

# Brute force ftw