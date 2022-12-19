file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

c = 0

sides = []
for line in l:
    line = line.strip()
    
    while "  " in line:
        line = line.replace("  ", " ")

    sides.append([int(j) for j in line.split()])

l = sides

print(l)

for iy in range(0, len(l), 3):
    for ix in range(3):
        sides = sorted([l[iy][ix], l[iy+1][ix], l[iy+2][ix]])

        if sides[0] + sides[1] > sides[2]:
            c += 1

print(c)