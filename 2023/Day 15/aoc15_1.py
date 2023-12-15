file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

l = l[0].split(",")

s = 0
for w in l:
    curr = 0
    for c in w:
        curr = (curr + ord(c)) * 17 % 256
    s += curr

print(s)