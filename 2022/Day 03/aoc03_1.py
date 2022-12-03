file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

s = 0
for i in l:
    a, b = i[:len(i) // 2], i[len(i) // 2:]
    c = [*set([*a]) & set([*b])][0]
    if c.isupper():
        s += ord(c) - ord("A") + 27
    else:
        s += ord(c) - ord("a") + 1

print(s)