file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

STEPS = 1000

pos = []
for i in l:
    x, y, z = i.split()
    x = int(x[3:-1])
    y = int(y[2:-1])
    z = int(z[2:-1])
    pos.append([x, y, z])

periods = []
for i in range(3):
    p = [j[i] for j in pos]
    v = [0] * len(p)
    gp, gv = p[:], v[:]

    steps = 0
    while 1:
        steps += 1

        for i in range(len(p)):
            for j in range(len(p)):
                if i == j:
                    continue

                v[i] += int(p[i] < p[j]) - int(p[i] > p[j])
        
        for i in range(len(p)):
            p[i] += v[i]
        
        if p == gp and v == gv:
            break
    
    periods.append(steps)

t = lcm(lcm(periods[0], periods[1]), periods[2])
print(t)