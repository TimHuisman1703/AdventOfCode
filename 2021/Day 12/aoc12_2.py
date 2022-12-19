file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

n = {}

for i in l:
    a, b = i.split("-")
    
    if a not in n.keys():
        n[a] = []
    if b not in n.keys():
        n[b] = []
    
    n[a] += [b]
    n[b] += [a]

queue = [("start", False)]
paths = set()

while queue:
    curr, used = queue.pop()
    path = curr.split("-")

    if path[-1] == "end":
        paths.add(curr)
        continue

    for a in n[path[-1]]:
        if a.isupper() or a not in path:
            queue += [(curr + "-" + a, used)]
        elif not used and a != "start":
            queue += [(curr + "-" + a, True)]

print(len(paths))