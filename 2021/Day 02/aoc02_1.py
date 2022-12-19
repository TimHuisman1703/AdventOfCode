file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

x = 0
y = 0
for i in l:
    d, s = i.split()
    s = int(s)

    if d[0] == "f":
        x += s
    
    if d[0] == "u":
        y -= s
    
    if d[0] == "d":
        y += s

print(x * y)