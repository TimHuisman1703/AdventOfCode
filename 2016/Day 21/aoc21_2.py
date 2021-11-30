file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

s = "fbgdceah"

rotate_based_reverse = {
	0: 1,
	1: 1,
	2: 6,
	3: 2,
	4: 7,
	5: 3,
	6: 0,
	7: 4,
}

for instr in l[::-1]:
	args = instr.split()

	if args[0] == "swap":
		if args[1] == "position":
			x, y = sorted([int(args[2]), int(args[5])])
			s = s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]
		elif args[1] == "letter":
			x, y = args[2], args[5]
			s = s.replace(x, "_").replace(y, x).replace("_", y)
	elif args[0] == "rotate":
		x = 0
		if args[1] == "left":
			x = -int(args[2])
		elif args[1] == "right":
			x = int(args[2])
		elif args[1] == "based":
			y = args[6]
			i = s.find(y)
			x = rotate_based_reverse[i]
		s = s[x:] + s[:x]
	elif args[0] == "reverse":
		x, y = int(args[2]), int(args[4])
		s = s[:x] + s[x:y+1][::-1] + s[y+1:]
	elif args[0] == "move":
		x, y = int(args[5]), int(args[2])
		c = s[x]
		s = s[:x] + s[x+1:]
		s = s[:y] + c + s[y:]

print(s)

# [V] swap position
# [V] swap letter
# [V] rotate left
# [V] rotate right
# [ ] rotate based
# [V] reverse
# [V] move