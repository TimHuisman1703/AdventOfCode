file = open("aoc06_input.txt")
l = [int(j) for j in file.read().split(",")]
file.close()

N = 80

for day in range(N):
    to_add = 0
    for i in range(len(l)):
        l[i] -= 1
        if l[i] == -1:
            to_add += 1
            l[i] = 6
    l += [8] * to_add

print(len(l))