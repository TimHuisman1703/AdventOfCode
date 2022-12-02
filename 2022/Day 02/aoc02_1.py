file = open("aoc02_input.txt")
l = [("ABC".index(j[0]), "XYZ".index(j[2])) for j in file.read().split("\n")]
file.close()

s = 0
for p in l:
    s += p[1] + 1 + 3 * ((p[1] - p[0] + 1) % 3)

print(s)