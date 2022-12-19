file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

from math import gcd

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

m = 0
for a in asteroids:
    seen = get_in_vision(asteroids, a)
    
    m = max(m, len(seen))

print(m)