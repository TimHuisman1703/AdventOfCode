file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

l = [[int(j) for j in row.split(",")] for row in l]

r = 0

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        ax = min(l[i][0], l[j][0])
        bx = max(l[i][0], l[j][0])
        ay = min(l[i][1], l[j][1])
        by = max(l[i][1], l[j][1])

        r = max(r, (bx - ax + 1) * (by - ay + 1))

print(r)