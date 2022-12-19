file = open("aoc17_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

target = 150

m = len(l)
c = 0

s = 0
for i in range(2**len(l)):
    b = [l[j] for j in range(len(l)) if (i>>j)&1]
    if sum(b) == target:
        if len(b) < m:
            s += 1
            m = len(b)
            c = 1
        elif len(b) == m:
            c += 1

print(m, c)