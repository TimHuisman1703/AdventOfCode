file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

def unpack(color):
	s = 0
	for i in l:
		if color == i[:len(color)]:
			if " no " in i:
				break

			w = i.split()
			for j in range(4, len(w), 4):
				s += int(w[j]) * unpack(w[j+1]+" "+w[j+2])
			return s+1
	return 1

print(unpack("shiny gold")-1)