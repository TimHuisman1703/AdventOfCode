file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

result = 0
for row in l:
	vals = sorted(int(j) for j in row.split())
	for i in range(len(vals)-1):
		for j in range(i+1, len(vals)):
			if vals[j] % vals[i] == 0:
				result += vals[j] // vals[i]

print(result)