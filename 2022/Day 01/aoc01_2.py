file = open("aoc01_input.txt")
l = file.read().split("\n")
file.close()

s = 0
a = []

for i in l:
    if i == "":
        a.append(s)
        s = 0
    else:
        s += int(i)
a.append(s)

a = sorted(a)

print(sum(a[-3:]))