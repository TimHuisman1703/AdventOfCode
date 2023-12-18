file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

wall = set([(0, 0)])
x = y = 0
for w in l:
    d, s, c = w.split()
    s = int(s)

    for _ in range(s):
        x += (d == "R") - (d == "L")
        y += (d == "D") - (d == "U")
        wall.add((x, y))

q = [(1, 1)]
inside = set()
while q:
    x, y = q.pop()

    if (x, y) in wall:
        continue

    if (x, y) in inside:
        continue
    inside.add((x, y))

    for d in range(4):
        q.append((
            x + (d == 0) - (d == 1),
            y + (d == 2) - (d == 3),
        ))

print(len(inside) + len(wall))