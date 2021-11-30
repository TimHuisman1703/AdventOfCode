file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

d = {}

all_food = set()
amount = {}

for i in l:
	s = i.split(" (contains ")
	food = set(s[0].split())
	allergens = s[1][:-1].split(", ")

	all_food |= food

	for j in food:
		if j in amount:
			amount.update({j: amount[j]+1})
		else:
			amount.setdefault(j, 1)

	for j in allergens:
		if j in d.keys():
			n = d[j] & food
			d.update({j: n})
		else:
			d.setdefault(j, food)

print(d)

while True:
	for i in d.keys():
		if len(d[i]) == 1:
			this_food = list(d[i])[0]
			for j in d.keys():
				if i == j:
					continue
				if this_food in d[j]:
					s = d[j]
					s.remove(this_food)
					d.update({j: s})
	
	looping = False
	for i in d.keys():
		if len(d[i]) > 1:
			looping = True
	if not looping:
		break

print(d)

rl = []
for i in sorted(d.keys()):
	rl.append(list(d[i])[0])

print(",".join(rl))