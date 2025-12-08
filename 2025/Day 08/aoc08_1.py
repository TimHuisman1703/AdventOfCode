file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

N = 1000

l = [[int(v) for v in row.split(",")] for row in l]

e = []
for i in range(len(l)):
    a = l[i]
    for j in range(i + 1, len(l)):
        b = l[j]
        diff = [b[c] - a[c] for c in range(3)]
        dist = sum(v ** 2 for v in diff)
        e.append((dist, i, j))

e = sorted(e)[::-1]

leader = [*range(len(l))]
while N:
    _, i, j = e.pop()

    if leader[i] != leader[j]:
        p = min(leader[i], leader[j])
        q = max(leader[i], leader[j])

        leader = [p if v == q else v for v in leader]
    
    N -= 1

d = {}
for v in leader:
    d[v] = d.get(v, 0) + 1

r = 1
for v in sorted(d.values())[::-1][:3]:
    r *= v

print(r)