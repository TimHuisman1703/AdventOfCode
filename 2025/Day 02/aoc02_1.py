file = open("aoc02_input.txt")
l = file.read().replace("\n", "")
file.close()

l = l.split(",")

r = 0
for i in l:
    print(">", i)
    a, b = [int(j) for j in i.split("-")]

    for x in range(a, b + 1):
        s = str(x)
        if 2 * s[:len(s) // 2] == s:
            r += x

print(r)