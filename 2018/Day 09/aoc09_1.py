file = open("aoc09_input.txt")
args = file.read().split()
file.close()

players = int(args[0])
last = int(args[6])

l = [0]
pos = 0
points = [0 for _ in range(players)]

i = 1
while i <= last:
	if i % 23:
		pos = (pos + 2) % len(l)
		l = l[:pos+1] + [i] + l[pos+1:]
	else:
		pos = (pos - 7) % len(l)
		points[(i-1) % players] += i + l[pos+1]
		l = l[:pos+1] + l[pos+2:]

	i += 1

	if i % 1000 == 999:
		print(f"{i+1}/{last}")

print(max(points))