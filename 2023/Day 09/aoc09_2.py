file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

s = 0
for w in l:
    d = [int(j) for j in w.split()]

    sign = 1
    while any(d):
        s += d[0] * sign
        d = [d[j + 1] - d[j] for j in range(len(d) - 1)]
        sign *= -1

print(s)