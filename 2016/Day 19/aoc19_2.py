file = open("aoc19_input.txt")
n = int(file.read())
file.close()

k = 0

for i in range(1, n+1):
	k += 1
	if 2*k > i:
		k += 1
	
	if k > i:
		k = 1

print(k)