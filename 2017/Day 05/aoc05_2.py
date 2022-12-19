file = open("aoc05_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

pos = 0
steps = 0

while pos > -1 and pos < len(l):
    new_pos = pos + l[pos]
    if l[pos] >= 3:
        l[pos] -= 1
    else:
        l[pos] += 1
    pos = new_pos
    steps += 1

print(steps)