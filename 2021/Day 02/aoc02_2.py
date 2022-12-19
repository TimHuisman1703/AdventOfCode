file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

x = 0
y = 0
a = 0
for i in l:
    d, s = i.split()
    s = int(s)

    if d[0] == "f":
        x += s
        y += s * a
    
    if d[0] == "u":
        a -= s
    
    if d[0] == "d":
        a += s

print(x * y)