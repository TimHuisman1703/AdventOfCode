file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

l = [int(j) for j in l]

r = 0
for x in l:
    for _ in range(2000):
        x = (x ^ (x * 64)) % 16777216
        x = (x ^ (x // 32)) % 16777216
        x = (x ^ (x * 2048)) % 16777216
    r += x

print(r)