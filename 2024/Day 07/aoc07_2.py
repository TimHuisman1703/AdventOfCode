file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

r = 0
for idx, w in enumerate(l):
    print(f"{idx=}")

    t, w = w.split(": ")
    t = int(t)
    w = [int(j) for j in w.split()]

    pos = False
    for i in range(3 ** (len(w) - 1)):
        c = w[0]
        for j in range(1, len(w)):
            ty = i // (3 ** (j - 1)) % 3
            if ty == 0:
                c *= w[j]
            elif ty == 1:
                c += w[j]
            else:
                c = int(str(c) + str(w[j]))
            
            if c > t:
                break
        
        if c == t:
            r += c
            break

print(r)