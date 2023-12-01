file = open("aoc01_input.txt")
l = file.read().split("\n")
file.close()

l = ["".join(j for j in w if j.isdigit()) for w in l]

s = 0
for w in l:
    s += int(w[0]) * 10 + int(w[-1])

print(s)