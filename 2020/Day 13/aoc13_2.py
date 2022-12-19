file = open("aoc13_input.txt")
l = file.read().split("\n")
file.close()

s = [j for j in l[1].split(",")]

b = []
for i in range(len(s)):
    if s[i] != "x":
        b.append(int(s[i]))
        b.append(int(i))

d = 1
j = 0
for i in range(0, len(b), 2):
    while (j+b[i+1]) % b[i]:
        j += d
    d *= b[i]

print(j)