file = open("aoc15_input.txt")
l = [int(j) for j in file.read().split(",")]
file.close()

d = {}
for i in range(len(l)):
    d.setdefault(l[i], i)

start = len(d)
end = 30000000

n = 0

for turn in range(start, end-1):
    try:
        key = n
        n = turn-d[key]
        d[key] = turn
    except:
        d.setdefault(n, turn)
        n = 0
print(turn+2, n)