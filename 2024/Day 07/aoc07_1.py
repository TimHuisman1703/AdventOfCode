file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

r = 0
for w in l:
    t, w = w.split(": ")
    t = int(t)
    w = [int(j) for j in w.split()]

    pos = False
    for i in range(1 << (len(w) - 1)):
        c = w[0]
        for j in range(1, len(w)):
            if i >> (j - 1) & 1:
                c *= w[j]
            else:
                c += w[j]
        
        if c == t:
            r += c
            break

print(r)