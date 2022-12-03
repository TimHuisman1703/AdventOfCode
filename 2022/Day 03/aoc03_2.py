file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

s = 0
for i in range(0, len(l), 3):
    c = [*set([*l[i]]) & set([*l[i + 1]]) & set([*l[i + 2]])][0]
    if c.isupper():
        s += ord(c) - ord("A") + 27
    else:
        s += ord(c) - ord("a") + 1

print(s)