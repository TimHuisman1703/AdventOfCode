file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

print(l)

x = y = 0
d = 0

for i in l:
    n = int(i[1:])

    if i[0] == "N":
        y -= n
    elif i[0] == "S":
        y += n
    elif i[0] == "W":
        x -= n
    elif i[0] == "E":
        x += n
    elif i[0] == "L":
        d = (d+n//90)%4
    elif i[0] == "R":
        d = (d+4-n//90)%4
    elif i[0] == "F":
        x += n*(int(d == 0) - int(d == 2))
        y += n*(int(d == 3) - int(d == 1))
    
    print(x, y, d)
print(abs(x) + abs(y))