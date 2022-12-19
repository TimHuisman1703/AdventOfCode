file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

s = 0
t = 0
for i in l:
    t += 1
    d = i.split()
    min, max = [int(j) for j in d[0].split("-")]
    c = d[1][0]
    if(min <= d[2].count(c) <= max):
        s += 1
        print(i)
print(s, t)