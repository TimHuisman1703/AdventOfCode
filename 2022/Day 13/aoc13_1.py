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

c = 0
for i in range(0, len(l), 3):
    a = eval(l[i])
    b = eval(l[i + 1])

    if f(a, b) <= 0:
        c += i // 3 + 1

print(c)