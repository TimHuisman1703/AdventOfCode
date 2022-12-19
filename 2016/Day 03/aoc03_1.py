file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

c = 0

for sides in l:
    sides = sides.strip()
    
    while "  " in sides:
        sides = sides.replace("  ", " ")
    
    sides = sorted([int(j) for j in sides.split()])

    if sides[0] + sides[1] > sides[2]:
        c += 1

print(c)