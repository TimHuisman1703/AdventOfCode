file = open("aoc07_input.txt")
l = [j.strip().split("\n") for j in file.read().split("$")][2:]
file.close()

nodes = {"/": ["/", None, [], {}]}
curr = nodes["/"]

for i in l:
    if i[0] == "cd ..":
        curr = nodes[curr[1]]
    elif i[0][:2] == "cd":
        child = i[0].split()[1]
        curr = nodes[curr[0] + child + "/"]
    elif i[0] == "ls":
        for j in i[1:]:
            if j.startswith("dir"):
                child = j.split()[1]
                if child not in curr[2]:
                    path = curr[0] + child + "/"
                    curr[2].append(path)
                    nodes[path] = [path, curr[0], [], {}]
            else:
                size, name = j.split()
                if name not in curr[3]:
                    curr[3][name] = int(size)

def f(node, needed):
    global l

    s = sum(node[3].values())
    m = 10 ** 20

    if node[2] == None:
        return s, m
    
    for child in node[2]:
        ts, tm = f(nodes[child], needed)
        s += ts
        m = min(m, tm)
    
    if s >= needed:
        m = min(m, s)
    
    return s, m

needed = f(nodes["/"], 0)[0] - 40000000
print(f(nodes["/"], needed)[1])