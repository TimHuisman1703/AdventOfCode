file = open("aoc19_input.txt")
l = file.read().split("\n")
file.close()

d = {}

for i in l[:-2]:
    a, b = i.split(" => ")
    if a not in d.keys():
        d[a] = []
    
    d[a] += [b]

m = l[-1]

s = set()
for i in range(len(m)):
    for key, value in d.items():
        if m[i:i+len(key)] == key:
            for j in value:
                s.add(m[:i] + j + m[i+len(key):])

print(len(s))