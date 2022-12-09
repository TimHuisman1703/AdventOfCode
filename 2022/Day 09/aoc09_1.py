file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

s = set([(0, 0)])

hx = hy = 0
tx = ty = 0

for i in l:
    a, b = i.split()
    b = int(b)

    for _ in range(b):
        hx += (a == "R") - (a == "L")
        hy += (a == "D") - (a == "U")
        
        if abs(tx - hx) > 1 or abs(ty -  hy) > 1:
            tx += (tx < hx) - (tx > hx)
            ty += (ty < hy) - (ty > hy)
        s.add((tx, ty))

print(len(s))