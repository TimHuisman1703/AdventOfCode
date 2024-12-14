file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

ps = []
vs = []
for w in l:
    pw, vw = w.split()
    ps.append([int(j) for j in pw[2:].split(",")])
    vs.append([int(j) for j in vw[2:].split(",")])

t = 0
while True:
    t += 1

    for i in range(len(ps)):
        ps[i][0] = (ps[i][0] + vs[i][0]) % 101
        ps[i][1] = (ps[i][1] + vs[i][1]) % 103

    g = [["." for _ in range(101)] for _ in range(103)]
    for x, y in ps:
        g[y][x] = "#"

    g = "\n".join("".join(row) for row in g)
    if "#" * 10 in g:
        print(g)
        print(t)
        break