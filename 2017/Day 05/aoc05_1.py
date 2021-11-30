file = open("aoc05_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

pos = 0
steps = 0

while pos > -1 and pos < len(l):
	l[pos] += 1
	pos += l[pos] - 1
	steps += 1

print(steps)