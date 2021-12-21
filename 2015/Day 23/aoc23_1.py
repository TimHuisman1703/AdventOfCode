file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

r = {"a": 0, "b": 0}
i = 0

while i < len(l):
	args = l[i].split()

	if args[0] == "hlf":
		r[args[1]] //= 2
		i += 1
	elif args[0] == "tpl":
		r[args[1]] *= 3
		i += 1
	elif args[0] == "inc":
		r[args[1]] += 1
		i += 1
	elif args[0] == "jmp":
		i += int(args[1])
	elif args[0] == "jie":
		if r[args[1][0]] % 2 == 0:
			i += int(args[2])
		else:
			i += 1
	elif args[0] == "jio":
		if r[args[1][0]] == 1:
			i += int(args[2])
		else:
			i += 1

print(r["a"], r["b"])