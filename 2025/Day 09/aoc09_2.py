file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

l = [[int(j) for j in row.split(",")] for row in l]

def sign(v):
    return (v > 0) - (v < 0)

paths = [
    [(l[-2][0] + 1, l[-2][1] + 1)],
    [(l[-2][0] - 1, l[-2][1] - 1)]
]
for i in range(len(l)):
    ax, ay = l[i - 2]
    bx, by = l[i - 1]
    cx, cy = l[i - 0]

    dx = sign(bx - ax) + sign(bx - cx)
    dy = sign(by - ay) + sign(by - cy)

    px = bx + dx
    py = by + dy
    qx = bx - dx
    qy = by - dy

    for x, y in [(px, py), (qx, qy)]:
        for path in paths:
            if x == path[-1][0] or y == path[-1][1]:
                path.append((x, y))
paths = [path[1:] for path in paths]

scores = []
for path in paths:
    s = 0
    for i in range(len(path)):
        ax = min(path[i - 1][0], path[i - 0][0])
        bx = max(path[i - 1][0], path[i - 0][0])
        ay = min(path[i - 1][1], path[i - 0][1])
        by = max(path[i - 1][1], path[i - 0][1])

        s += (bx - ax + 1) * (by - ay + 1) - 1
    scores.append(s)

if scores[0] > scores[1]:
    path = paths[0]
else:
    path = paths[1]

r = 0
for i in range(len(l)):
    print(f"> {i} / {len(l)}")
    for j in range(i + 1, len(l)):
        ax = min(l[i][0], l[j][0])
        bx = max(l[i][0], l[j][0])
        ay = min(l[i][1], l[j][1])
        by = max(l[i][1], l[j][1])

        area = (bx - ax + 1) * (by - ay + 1)
        if area <= r:
            continue

        pos = True
        for k in range(len(path)):
            px, py = path[k - 1]
            qx, qy = path[k - 0]
            px, qx = min(px, qx), max(px, qx)
            py, qy = min(py, qy), max(py, qy)

            if px == qx:
                if ax <= px <= bx and not (qy < ay or py > by):
                    pos = False
                    break
            else:
                if ay <= py <= by and not (qx < ax or px > bx):
                    pos = False
                    break

        if pos:
            r = area

print(r)