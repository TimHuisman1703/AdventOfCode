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
        for n in range(1, len(s) // 2 + 1):
            if s[:n] * (len(s) // n) == s:
                r += x
                break

print(r)