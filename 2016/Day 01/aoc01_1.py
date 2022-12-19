file = open("aoc01_input.txt")
l = file.read().split(", ")
file.close()

d = [0, 0]
dir = [0, 1]

for move in l:
    turn, steps = move[0], int(move[1:])

    if turn == "L":
        dir = [-dir[1], dir[0]]
    else:
        dir = [dir[1], -dir[0]]
    
    d[0] += steps * dir[0]
    d[1] += steps * dir[1]

print(abs(d[0]) + abs(d[1]))