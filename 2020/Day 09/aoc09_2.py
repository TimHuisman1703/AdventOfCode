file = open("aoc09_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

x = 105950735

for i in range(0, len(l)):
	for j in range(i+2, len(l)+1):
		if sum(l[i:j]) == x:
			print(l[i:j], sum(l[i:j]))
			m = max(l[i:j])
			n = min(l[i:j])
			print(m, n, m+n)
		elif sum(l[i:j]) > x:
			break