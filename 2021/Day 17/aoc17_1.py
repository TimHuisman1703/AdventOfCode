file = open("aoc17_input.txt")
l = file.read().split()
file.close()

min_x, max_x = [int(j) for j in l[2][2:-1].split("..")]
min_y, max_y = [int(j) for j in l[3][2:].split("..")]

print(-min_y * (-min_y - 1) // 2)