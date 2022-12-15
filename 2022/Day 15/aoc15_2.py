file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

M = 4000000

s = []

for i in l:
    i = i.split()
    sx, sy = int(i[2][2:-1]), int(i[3][2:-1])
    bx, by = int(i[8][2:-1]), int(i[9][2:])

    r = abs(sx - bx) + abs(by - sy)
    s.append((sx, sy, r))

for i in range(len(s)):
    ax, ay, ar = s[i]
    print(f"{i + 1}/{len(s)}")
    
    for nx in range(max(0, ax - ar - 1), min(M + 1, ax + ar + 2)):
        for side in range(1 + (-ar <= nx <= ar)):
            ny = ay + (ar + 1 - abs(nx - ax)) * (2 * side - 1)
            if ny < 0 or ny > M:
                continue

            for b in s:
                bx, by, br = b
                if abs(bx - nx) + abs(by - ny) <= br:
                    break
            else:
                print(nx * 4000000 + ny)
                exit()