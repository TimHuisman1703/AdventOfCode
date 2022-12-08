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

def f(node):
    s = sum(node[3].values())
    c = 0

    if node[2] == None:
        return s, c
    
    for child in node[2]:
        ts, tc = f(nodes[child])
        s += ts
        c += tc
    
    if s <= 100000:
        c += s
    
    return s, c

print(f(nodes["/"])[1])