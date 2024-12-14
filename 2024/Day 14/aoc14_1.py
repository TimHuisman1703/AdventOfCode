file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

c = [0, 0, 0, 0]

for w in l:
    pw, vw = w.split()
    px, py = [int(j) for j in pw[2:].split(",")]
    vx, vy = [int(j) for j in vw[2:].split(",")]

    for _ in range(100):
        px = (px + vx) % 101
        py = (py + vy) % 103
    
    if px != 50 and py != 51:
        c[(px < 50) + 2 * (py < 51)] += 1

p = 1
for x in c:
    p *= x

print(p)