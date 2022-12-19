file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

d = {}
references = {"ORE": 1}

for i in l:
    a, b = i.split(" => ")

    r = set()
    for j in a.split(", "):
        c, m = j.split()
        r.add((int(c), m))

        if m not in references.keys():
            references[m] = 0
        references[m] += 1
    
    c, m = b.split()
    d[m] = (int(c), r)

    if m not in references.keys():
        references[m] = 0
    references[m] += 1

needed = {key: int(key == "FUEL") for key in references.keys()}

while references:
    m = sorted(references, key=lambda x: references[x])[0]
    references.pop(m)
    
    if m == "ORE":
        print(needed[m])
        break
    
    c, r = d[m]
    n = (needed[m] - 1) // c + 1

    for c, i in r:
        references[i] -= 1
        needed[i] += c * n