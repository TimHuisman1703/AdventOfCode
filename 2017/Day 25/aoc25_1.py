file = open("aoc25_input.txt")
l = file.read().split("\n\n")
file.close()

args = l[0].split()
state = args[3][0]
steps = int(args[9])

instructions = {}

for s in l[1:]:
	args = s.split()

	key = args[2][0]
	instr = []
	for expectation in range(2):
		write = int(args[13 + 23 * expectation][0])
		step = 1 - 2 * int(args[20 + 23 * expectation][0] == "l")
		next = args[25 + 23 * expectation][0]

		instr.append((write, step, next))
	
	instructions.update({key: instr})

pos = 0
ones = set()

for iter in range(steps):
	write, step, next = instructions[state][pos in ones]
	
	if write:
		if pos not in ones:
			ones.add(pos)
	else:
		if pos in ones:
			ones.remove(pos)
	
	pos += step
	state = next

	if iter % 1000000 == 999999:
		print(f"Passed {iter+1}")

print(len(ones))