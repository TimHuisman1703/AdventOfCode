file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

i = 0
x = 1
c = 0
a = 10 ** 10

s = 0

while i < len(l):
    if c % 40 == 19:
        s += x * (c + 1)
    c += 1
    
    if a != 10 ** 10:
        x += a
        a = 10 ** 10
    else:
        if l[i] != "noop":
            a = int(l[i].split()[1])
        i += 1

print(s)