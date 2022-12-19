file = open("aoc03_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

x = y = 0
s = set()
s.add("0,0")

for i in l[0]:
    if i == "^":
        y -= 1
    elif i == "v":
        y += 1
    elif i == "<":
        x -= 1
    else:
        x += 1
    s.add(f"{x},{y}")

print(len(s))