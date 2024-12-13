file = open("aoc13_input.txt")
l = file.read().split("\n\n")
file.close()

r = 0
for w in l:
    w = w.split("\n")
    ax, ay = [int(j[2:]) for j in w[0].split(": ")[1].split(", ")]
    bx, by = [int(j[2:]) for j in w[1].split(": ")[1].split(", ")]
    tx, ty = [int(j[2:]) for j in w[2].split(": ")[1].split(", ")]

    i = 0
    while ax * i <= tx and ay * i <= ty:
        if (tx - ax * i) % bx == 0 and (ty - ay * i) % by == 0 and (tx - ax * i) // bx == (ty - ay * i) // by:
            j = (tx - ax * i) // bx
            r += i * 3 + j
            break

        i += 1

print(r)