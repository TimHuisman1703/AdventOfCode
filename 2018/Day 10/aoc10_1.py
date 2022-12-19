file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

TIME_OFFSET = 10000

pos = []
vel = []

for s in l:
    args = s.replace(",", "").split("> velocity=<")

    args[0] = args[0][10:]
    x, y = [int(j) for j in args[0].split()]

    args[1] = args[1][:-1]
    vx, vy = [int(j) for j in args[1].split()]

    pos.append((x + TIME_OFFSET * vx, y + TIME_OFFSET * vy))
    vel.append((vx, vy))

last_min_y = None
t = 0
while 1:
    min_y = min(pos[j][0] + t * vel[j][0] for j in range(len(pos)))

    if last_min_y != None and min_y < last_min_y:
        break
    last_min_y = min_y
    t += 1

t -= 1
current_pos = [(pos[j][0] + t * vel[j][0], pos[j][1] + t * vel[j][1]) for j in range(len(pos))]

min_x = min(j[0] for j in current_pos)
max_x = max(j[0] for j in current_pos)
min_y = min(j[1] for j in current_pos)
max_y = max(j[1] for j in current_pos)

g = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

for ix, iy in current_pos:
    g[iy - min_y][ix - min_x] = "#"

print("\n".join("".join(row) for row in g))