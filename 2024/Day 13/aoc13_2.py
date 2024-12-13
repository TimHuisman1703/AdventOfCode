file = open("aoc13_input.txt")
l = file.read().split("\n\n")
file.close()

r = 0
for w in l:
    w = w.split("\n")
    ax, ay = [int(j[2:]) for j in w[0].split(": ")[1].split(", ")]
    bx, by = [int(j[2:]) for j in w[1].split(": ")[1].split(", ")]
    tx, ty = [int(j[2:]) + 10000000000000 for j in w[2].split(": ")[1].split(", ")]

    # y = x * (ay / ax)
    # (y - ty) = (x - tx) * (by / bx)
    #
    # y = x * (by / bx) - tx * (by / bx) + ty = x * (ay / ax)
    # x * (by / bx - ay / ax) - tx * (by / bx) + ty = 0
    # x * (by / bx - ay / ax) = tx * (by / bx) - ty
    # x = (tx * (by / bx) - ty) / (by / bx - ay / ax)
    # x = (tx * ax * by - ty * ax * bx) / (ax * by - bx * ay)

    num = tx * ax * by - ty * ax * bx
    den = ax * by - bx * ay
    if num % den != 0:
        continue

    x = num // den
    if x % ax != 0:
        continue

    pa = x // ax
    pbx = (tx - ax * pa) // bx
    pby = (ty - ay * pa) // by
    if pbx == pby:
        r += 3 * pa + pbx

print(r)