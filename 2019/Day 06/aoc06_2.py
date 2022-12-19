file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

parent = {}

for i in l:
    a, b = i.split(")")
    parent[b] = a

curr = parent["YOU"]
path_you = {curr: 0}
while 1:
    cost = path_you[curr]
    curr = parent[curr]
    path_you[curr] = cost + 1

    if curr == "COM":
        break

curr = parent["SAN"]
cost = 0
while 1:
    try:
        print(path_you[curr] + cost)
        break
    except:
        pass

    curr = parent[curr]
    cost += 1