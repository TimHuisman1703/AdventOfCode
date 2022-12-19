file = open("aoc19_input.txt")
n = int(file.read())
file.close()

k = 1

while 2*k <= n:
    k <<= 1

print(2*(n-k) + 1)