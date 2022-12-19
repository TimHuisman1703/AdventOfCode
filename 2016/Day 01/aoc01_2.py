file = open("aoc01_input.txt")
l = file.read().split(", ")
file.close()

d = [0, 0]
dir = [0, 1]

visited = set([(0, 0)])

for move in l:
    turn, steps = move[0], int(move[1:])

    if turn == "L":
        dir = [-dir[1], dir[0]]
    else:
        dir = [dir[1], -dir[0]]
    
    for i in range(steps):
        d[0] += dir[0]
        d[1] += dir[1]

        if (d[0], d[1]) in visited:
            print(abs(d[0]) + abs(d[1]))
            exit()
        else:
            visited.add((d[0], d[1]))