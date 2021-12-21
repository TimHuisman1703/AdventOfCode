file = open("aoc19_input.txt")
l = file.read().split("\n")
file.close()

for i in range(len(l)):
	l[i] = l[i] \
		.replace("Al", "A") \
		.replace("Ar", "G") \
		.replace("Ca", "D") \
		.replace("e", "E") \
		.replace("Mg", "M") \
		.replace("Rn", "R") \
		.replace("Si", "S") \
		.replace("Th", "T") \
		.replace("Ti", "U")

d = {}

i = 0
while l[i]:
	a, b = l[i].split(" => ")
	if a not in d.keys():
		d[a] = []
	
	d[a] += [b]
	i += 1

s = l[i+1]

print(len(s))