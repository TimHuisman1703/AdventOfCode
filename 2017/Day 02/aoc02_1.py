file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

result = 0
for row in l:
    vals = [int(j) for j in row.split()]
    result += max(vals) - min(vals)

print(result)