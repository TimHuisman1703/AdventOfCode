file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

x = int(l[0].split()[4])
y = int(l[1].split()[4])

a = b = 0

steps = 0
while a < 1000 and b < 1000:
    steps += 1

    if steps % 2 == 1:
        x = (x + 9 * steps - 4) % 10 + 1
        a += x
    else:
        y = (y + 9 * steps - 4) % 10 + 1
        b += y

print(3 * steps * min(a, b))