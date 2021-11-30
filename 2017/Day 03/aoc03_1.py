file = open("aoc03_input.txt")
n = int(file.read())
file.close()

k = 1
while (k+2)**2 < n:
	k += 2

a = (n - (k*k + 1)) % (k+1)
print((k+1) // 2 + abs(a - (k-1) // 2))