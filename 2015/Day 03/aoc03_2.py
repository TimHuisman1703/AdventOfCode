file = open("aoc03_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

x = [0, 0]
y = [0, 0]
s = set()
s.add("0,0")

for i in range(len(l[0])):
    if l[0][i] == "^":
        y[i%2] -= 1
    elif l[0][i] == "v":
        y[i%2] += 1
    elif l[0][i] == "<":
        x[i%2] -= 1
    else:
        x[i%2] += 1
    s.add(f"{x[i%2]},{y[i%2]}")

print(len(s))