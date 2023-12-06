file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

ts = [int(j) for j in l[0].split()[1:]]
ds = [int(j) for j in l[1].split()[1:]]

p = 1
for t, d in zip(ts, ds):
    s = 0
    for i in range(0, t):
        b = i * (t - i)
        if b > d:
            s += 1
    p *= s

print(p)