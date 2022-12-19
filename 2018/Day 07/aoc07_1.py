file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

req = {}

for instr in l:
    args = instr.split()

    if args[1] not in req.keys():
        req.update({args[1]: []})
    if args[7] not in req.keys():
        req.update({args[7]: []})
    
    req[args[7]].append(args[1])

path = ""

while req:
    possible = sorted(req.keys())
    
    for c in possible:
        if all(j not in req.keys() for j in req[c]):
            path += c
            req.pop(c)
            break

print(path)