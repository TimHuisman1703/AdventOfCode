file = open("aoc08_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

s = 0

for i in l:
    s += len(i) - len(eval(i))

print(s)