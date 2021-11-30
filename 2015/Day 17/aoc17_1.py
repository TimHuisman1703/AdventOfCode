file = open("aoc17_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

target = 150

s = 0
for i in range(2**len(l)):
	if sum([l[j] for j in range(len(l)) if (i>>j)&1]) == target:
		s += 1

print(s)