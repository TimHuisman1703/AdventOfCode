file = open("aoc12_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

t = l[0]
s = 0
i = 0
while i < len(t):
    if t[i] == "-" or t[i].isdigit():
        e = i+1
        while t[e].isdigit():
            e += 1
        s += int(t[i:e])
        i = e
    i += 1

print(s)