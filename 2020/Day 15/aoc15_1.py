file = open("aoc15_input.txt")
values = [int(j) for j in file.read().split(",")]
file.close()

turnsAgo = [int(j) for j in range(len(values))[::-1]]

start = len(values)
end = 2020

n = 0

for turn in range(start, end-1):

    for j in range(len(turnsAgo)):
        turnsAgo[j] += 1
    
    if n in values:
        index = values.index(n)
        n = turnsAgo[index]
        turnsAgo[index] = 0
    else:
        values.append(n)
        turnsAgo.append(0)
        n = 0
print(turn+2, n)