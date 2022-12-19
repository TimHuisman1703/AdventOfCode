file = open("aoc03_input.txt")
n = int(file.read())
file.close()

g = [[0] * 51 for _ in range(51)]
g[25][25] = 1

dir = (1, 0)
x, y = 25, 25
turn = 1
step_size = 1
time_till_turn = 1

while True:
    dx, dy = dir
    x += dx
    y += dy
    time_till_turn -= 1
    turn += 1

    if time_till_turn == 0:
        dir = (dir[1], -dir[0])

        if dir[1] == 0:
            step_size += 1
        
        time_till_turn = step_size
    
    sum = 0
    for ix in range(x-1, x+2):
        for iy in range(y-1, y+2):
            sum += g[iy][ix]
    
    g[y][x] = sum
    
    if sum > n:
        print(sum)
        break