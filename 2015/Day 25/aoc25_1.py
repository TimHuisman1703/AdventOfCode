file = open("aoc25_input.txt")
l = file.read().split()
file.close()

y = int(l[15][:-1])
x = int(l[17][:-1])

a = x + y - 2
b = a * (a + 1) // 2 + x - 1
print(f"Buckle up, we're gonna iterate {b} times!")

c = 20151125
for i in range(b):
    c = (c * 252533) % 33554393

print(c)