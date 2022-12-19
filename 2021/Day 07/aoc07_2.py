file = open("aoc07_input.txt")
l = [int(j) for j in file.read().split(",")]
file.close()

m = 10**100

for i in range(min(l), max(l) + 1):
    c = 0
    for crab in l:
        n = abs(crab - i)
        c += n * (n + 1) // 2
    if c < m:
        m = c

print(m)