file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

t = int("".join(l[0].split()[1:]).replace(" ", ""))
d = int("".join(l[1].split()[1:]).replace(" ", ""))

a = 0
b = t // 2
while a != b:
    mid = (a + b) // 2

    if mid * (t - mid) > d:
        b = mid
    else:
        a = mid + 1

print(t - a * 2 + 1)