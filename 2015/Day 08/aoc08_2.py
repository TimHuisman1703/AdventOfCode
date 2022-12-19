file = open("aoc08_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

s = 0

for i in l:
    s += 2 + len(i.replace("\\", "\\\\").replace("\"", "\\\"").replace("'", "\\'"))-len(i)

print(s)