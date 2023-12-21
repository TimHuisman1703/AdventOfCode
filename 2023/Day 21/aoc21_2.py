file = open("aoc21_input.txt")
g = file.read().split("\n")
file.close()

g = [list(j) for j in g]
w, h = len(g[0]), len(g)

sx = sy = 0
for iy in range(h):
    for ix in range(w):
        if g[iy][ix] == "S":
            sx, sy = ix, iy
        g[iy][ix] = g[iy][ix] == "#"

g = [[g[jy % h][jx % w] for jx in range(2 * w)] for jy in range(2 * h)]
w *= 2
h *= 2

timeline = [[] for _ in range(9)]
p = set([(sx, sy)])
visited = [set([*p]), set()]
visited_per_region = [[set(), set()] for _ in range(9)]

steps = 0
while True:
    np = set()
    for x, y in p:
        for d in range(4):
            nx = x + (d == 0) - (d == 1)
            ny = y + (d == 2) - (d == 3)

            if nx < -w or nx >= 2 * w or ny < -h or ny >= 2 * h:
                continue

            key = (nx, ny)
            if g[ny % h][nx % w]:
                continue

            v = visited[steps % 2]
            if key in v:
                continue
            v.add(key)

            for idx in range(9):
                if -w <= nx - (idx % 3) * w < 0 and -h <= ny - (idx // 3) * h < 0:
                    visited_per_region[idx][steps % 2].add(key)

            np.add(key)

    p = np
    steps += 1

    for idx in range(9):
        c = len(visited_per_region[idx][steps % 2])
        timeline[idx].append(c)

    if len(timeline[0]) >= 3:
        for idx in range(9):
            if timeline[idx][-1] != timeline[idx][-3]:
                break
        else:
            break

    if steps % 100 == 0:
        print(f"steps = {steps}")

def take(t, idx):
    if idx >= len(t):
        idx -= (idx - len(t) + 2) // 2 * 2
    return t[idx]

N = 26501365

# Mid
t = timeline[4]
mid = take(t, N)

# Corners
corners = 0
for idx in [0, 2, 6, 8]:
    t = timeline[idx]

    one = t.index(1)
    a, b = divmod(N - one, w)
    a += 1

    # Shell
    for inward in range(2):
        i = one + b + inward * w
        corners += take(t, i) * max(a - inward, 0)

    # Interior
    if a > 0:
        x = max(a, 0)
        p = max((x - 1) * (x - 2) // 2, 0)

        corners += p * take(t, N + 1)

# Axes
axes = 0
for idx in [1, 3, 5, 7]:
    t = timeline[idx]

    one = t.index(1)
    a, b = divmod(N - one, w)
    a += 1

    # Shell
    for inward in range(2):
        if a - inward <= 0:
            continue
        i = one + b + inward * w
        axes += take(t, i)

    # Interior
    p = max(a - 2, 0)
    axes += p * take(t, N)

print(mid + corners + axes)