file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

s = set(l)
a = ""
for i in range(len(l[0])):
    ones = 0
    zeros = 0
    for j in s:
        if j[0] == "0":
            zeros += 1
        else:
            ones += 1

    if ones >= zeros:
        a += "1"
    else:
        a += "0"
    
    ns = set()
    for j in s:
        if j[0] == a[-1]:
            ns.add(j[1:])
    
    s = ns

a = int(a, 2)

s = set(l)
b = ""
for i in range(len(l[0])):
    if len(s) == 1:
        break

    ones = 0
    zeros = 0
    for j in s:
        if j[0] == "0":
            zeros += 1
        else:
            ones += 1

    if ones < zeros:
        b += "1"
    else:
        b += "0"
    
    ns = set()
    for j in s:
        if j[0] == b[-1]:
            ns.add(j[1:])
    
    s = ns

b = int(b + list(s)[0], 2)

print(a, b)

print(a * b)