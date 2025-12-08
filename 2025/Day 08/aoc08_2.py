file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

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

n = len(l)
leader = [*range(n)]
while n > 1:
    _, i, j = e.pop()

    if leader[i] != leader[j]:
        p = min(leader[i], leader[j])
        q = max(leader[i], leader[j])

        leader = [p if v == q else v for v in leader]
        n -= 1

a = l[i]
b = l[j]
r = a[0] * b[0]

print(r)