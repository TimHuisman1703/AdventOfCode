file = open("aoc01_input.txt")
l = file.read().split("\n")
file.close()

s = 0
m = 0

for i in l:
    if i == "":
        m = max(m, s)
        s = 0
    else:
        s += int(i)
m = max(m, s)

print(m)