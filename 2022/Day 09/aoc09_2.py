file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

s = set([(0, 0)])

x = [0] * 10
y = [0] * 10

for i in l:
    a, b = i.split()
    b = int(b)

    for _ in range(b):
        x[0] += (a == "R") - (a == "L")
        y[0] += (a == "D") - (a == "U")
        
        for j in range(len(x) - 1):
            if abs(x[j + 1] - x[j]) > 1 or abs(y[j + 1] -  y[j]) > 1:
                x[j + 1] += (x[j + 1] < x[j]) - (x[j + 1] > x[j])
                y[j + 1] += (y[j + 1] < y[j]) - (y[j + 1] > y[j])
        s.add((x[-1], y[-1]))

print(len(s))