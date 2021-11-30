file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

i = 1

cards = [[], []]
while l[i] != "":
	cards[0].append(int(l[i]))
	i += 1

i += 2
while i < len(l):
	cards[1].append(int(l[i]))
	i += 1

while len(cards[0]) and len(cards[1]):
	top = [-1, -1]
	for i in range(2):
		top[i] = cards[i][0]
		cards[i] = cards[i][1:]

	if top[0] > top[1]:
		cards[0].append(top[0])
		cards[0].append(top[1])
	else:
		cards[1].append(top[1])
		cards[1].append(top[0])
	
	print(cards)

winner = int(len(cards[1]) > 0)

p = 0
for i in range(len(cards[winner])):
	p += (len(cards[winner])-i)*cards[winner][i]
print(p)