file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

l = [[int(j) for j in row] for row in l]

def flood_fill(x, y):
    global l

    queue = [(x, y)]
    l[y][x] = -1
    result = 0

    while queue:
        result += 1
        x, y = queue.pop()

        if x > 0:
            if l[y][x-1] > -1 and l[y][x-1] < 9:
                l[y][x-1] = -1
                queue.append((x-1, y))
        if x < len(l[0]) - 1:
            if l[y][x+1] > -1 and l[y][x+1] < 9:
                l[y][x+1] = -1
                queue.append((x+1, y))
        if y > 0:
            if l[y-1][x] > -1 and l[y-1][x] < 9:
                l[y-1][x] = -1
                queue.append((x, y-1))
        if y < len(l) - 1:
            if l[y+1][x] > -1 and l[y+1][x] < 9:
                l[y+1][x] = -1
                queue.append((x, y+1))
    
    return result    

c = []

for iy in range(len(l)):
    for ix in range(len(l[0])):
        if l[iy][ix] > -1 and l[iy][ix] < 9:
            c.append(flood_fill(ix, iy))

c = sorted(c)[::-1]
print(c[0] * c[1] * c[2])