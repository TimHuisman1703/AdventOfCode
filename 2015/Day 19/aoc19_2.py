file = open("aoc19_input.txt")
l = file.read().split("\n")
file.close()

import heapq

d = {}
for i in l[:-2]:
	a, b = i.split(" => ")
	d[b] = a

steps = l[-1].count("Ca")
m = l[-1].replace("Ca", "")

q = [(0, steps, m)]
visited = set()
while 1:
	cost, steps, s = heapq.heappop(q)

	if s in visited:
		continue
	visited.add(s)

	if s == "e":
		print(steps)
		exit()

	for key, value in d.items():
		i = s.find(key)
		while i > -1:
			ns = s[:i] + value + s[i+len(key):]
			if ns not in visited:
				heapq.heappush(q, (steps + len(ns), steps + 1, ns))
			i = s.find(key, i+1)