file = open("aoc18_input.txt")
first_row = file.read()
file.close()

height = 40

width = len(first_row)
row = [int(j == "^") for j in first_row]
c = row.count(0)

for _ in range(height - 1):
	row = [0] + row + [0]
	row = [row[j] ^ row[j+2] for j in range(width)]
	c += row.count(0)

print(c)