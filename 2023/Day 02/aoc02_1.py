file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

s = 0
for i in range(len(l)):
    b = l[i].split(": ")[1].split("; ")
    pos = True

    for g in b:
        count = {}
        for w in g.split(", "):
            n, t = w.split()
            count[t] = count.get(t, 0) + int(n)

        if count.get("red", 0) > 12 or count.get("green", 0) > 13 or count.get("blue", 0) > 14:
            pos = False
            break

    if pos:
        s += i + 1

print(s)