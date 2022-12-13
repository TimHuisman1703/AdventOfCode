file = open("aoc13_input.txt")
l = file.read().split("\n")
file.close()

def f(a, b):
    if type(a) == type(b) == int:
        return (a > b) - (a < b)
    
    if type(a) == int:
        a = [a]
    elif type(b) == int:
        b = [b]
    
    for i in range(min(len(a), len(b))):
        x = f(a[i], b[i])
        if x != 0:
            return x
    return (len(a) > len(b)) - (len(a) < len(b))

p = [[[2]], [[6]]]
for i in range(0, len(l), 3):
    p.append(eval(l[i]))
    p.append(eval(l[i + 1]))

i = 0
while i < len(p) - 1:
    if f(p[i], p[i + 1]) == 1:
        p[i], p[i + 1] = p[i + 1], p[i]
        i = max(0, i - 1)
    else:
        i += 1

print((p.index([[2]]) + 1) * (p.index([[6]]) + 1))