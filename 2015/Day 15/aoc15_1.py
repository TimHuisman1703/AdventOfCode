file = open("aoc15_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

def outcome(attr, div):
	total = 1
	for i in range(4):
		s = 0
		for j in range(len(attr)):
			s += div[j]*attr[j][i]
		total *= max(0, s)
	return total

attr = []
for i in l:
	s = (i+",").split()
	curr_attr = [int(s[2][:-1]), int(s[4][:-1]), int(s[6][:-1]), int(s[8][:-1]), int(s[10][:-1])]
	attr.append(curr_attr)

n = 100 // len(attr)
div = [n] * (len(attr) - 1)
div.append(100-sum(div))
last, current = 0, outcome(attr, div)
while current == 0 or last != current:
	last = current
	for i in range(len(attr)):
		for j in range(len(attr)):
			if i == j:
				continue
			if div[i] > 99 or div[j] < 1:
				continue
			new_div = [k for k in div]
			new_div[i] += 1
			new_div[j] -= 1
			curr_outcome = outcome(attr, new_div)
			if curr_outcome > current:
				print(new_div, curr_outcome)
				current = curr_outcome
				div = new_div
print(current)