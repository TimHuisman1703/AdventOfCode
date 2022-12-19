file = open("aoc01_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

s = 0
for i in l:
    s += i // 3 - 2

print(s)