file = open("aoc01_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

f = 0
for i in range(len(l[0])):
    f += 1 if l[0][i] == "(" else -1
    if f < 0:
        print(i+1)
        break