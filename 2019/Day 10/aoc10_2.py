file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

from math import gcd
from numpy import angle

N = 200

asteroids = set()
for iy in range(len(l)):
	for ix in range(len(l[0])):
		if l[iy][ix] == "#":
			asteroids.add((ix, iy))

def get_in_vision(asteroids, a):
	seen = {}

	for b in asteroids:
		dist = (b[0] - a[0], b[1] - a[1])

		if dist == (0, 0):
			continue
		
		if dist[0] == 0:
			key = (0, dist[1] // abs(dist[1]))
		elif dist[1] == 0:
			key = (dist[0] // abs(dist[0]), 0)
		else:
			d = gcd(dist[0], dist[1])
			key = (dist[0] // d, dist[1] // d)
		
		if key in seen.keys():
			if abs(sum(seen[key])) < abs(sum(dist)):
				continue
		
		seen[key] = dist
	
	return seen

best = (0, (0, 0))
for a in asteroids:
	seen = get_in_vision(asteroids, a)
	
	if best[0] < len(seen):
		best = (len(seen), a)

x, y = best[1]
destroyed = 0

while 1:
	in_vision = get_in_vision(asteroids, (x, y))
	keys = sorted([*in_vision.keys()], key=lambda a: -angle(a[1] + a[0] * 1j))

	for k in keys:
		dist = in_vision[k]
		b = (x + dist[0], y + dist[1])

		destroyed += 1
		if destroyed == N:
			print(100 * b[0] + b[1])
			exit()
		
		asteroids.remove(b)