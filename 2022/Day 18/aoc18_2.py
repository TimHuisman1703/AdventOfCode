file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

c = set(tuple(int(k) for k in j.split(",")) for j in l)

q = [(0, 0, 0)]
v = set()
s = 0

while q:
    curr = q.pop()

    if curr in c:
        s += 1
        continue
    
    if curr in v:
        continue
    v.add(curr)

    for j in range(6):
        x, y, z = [curr[k] - (k == j) + (k + 3 == j) for k in range(3)]
        if -5 <= x <= 25 and -5 <= y <= 25 and -5 <= z <= 25:
            q.append((x, y, z))

print(s)