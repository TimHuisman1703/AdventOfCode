file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

def f(s, idx, l):
    if idx >= len(s) - 1:
        if not l:
            return 1
        else:
            return 0

    if s[idx] == "#" and not l:
        return 0
    if len(s) - idx < sum(l) + len(l):
        return 0

    r = 0
    if s[idx] != "#":
        r += f(s, idx + 1, l)
    if s[idx] in "#?" and l:
        p = l.pop()
        pos = s[idx + p] in ".?"
        for i in range(p):
            if s[idx + i] not in "#?":
                pos = False
                break
        if pos:
            r += f(s, idx + p + 1, l)
        l.append(p)

    return r

s = 0
for w in l:
    a, b = w.split()
    b = [int(j) for j in b.split(",")][::-1]

    a += "."

    x = f(a, 0, b)
    s += x

print(s)