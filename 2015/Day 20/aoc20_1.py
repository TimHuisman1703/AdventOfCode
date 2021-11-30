file = open("aoc20_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

house = 1
for house in range(1, 10001):
	s = 0
	for j in range(1, house+1):
		if house % j == 0:
			s += j
	print(house, s)
	house += 1