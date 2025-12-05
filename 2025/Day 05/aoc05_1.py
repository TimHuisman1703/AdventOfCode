file = open("aoc05_input.txt")
l = file.read()
file.close()

la, lb = l.split("\n\n")

l = []
for i in la.split():
    a, b = [int(j) for j in i.split("-")]
    l.append((a, b))

r = 0
for v in lb.split():
    v = int(v)

    for a, b in l:
        if a <= v <= b:
            r += 1
            break

print(r)