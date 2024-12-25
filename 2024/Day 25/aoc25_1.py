file = open("aoc25_input.txt")
l = file.read().split("\n\n")
file.close()

keys = []
locks = []
for w in l:
    w = w.split("\n")
    w = [[w[jy][jx] for jy in range(7)] for jx in range(5)]

    if w[0][0] == "#":
        h = [j.index(".") for j in w]
        keys.append(h)
    else:
        h = [j.index("#") for j in w]
        locks.append(h)

r = 0
for key in keys:
    for lock in locks:
        r += all(k <= l for k, l in zip(key, lock))

print(r)