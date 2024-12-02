file = open("aoc02_input.txt")
g = [[int(j) for j in row.split()] for row in file.read().split("\n")]
file.close()

x = 0
for l in g:
    pos = 0
    for i in range(len(l)):
        row = l[:i] + l[i+1:]
        if row == sorted(row) or row == sorted(row)[::-1]:
            for i in range(len(row) - 1):
                if abs(row[i] - row[i + 1]) > 3:
                    break
                if abs(row[i] - row[i + 1]) == 0:
                    break
            else:
                pos = 1
    x += pos

print(x)