file = open("aoc06_input.txt")
l = [int(j) for j in file.read().split()]
file.close()

seen = []

while True:
    if str(l) in seen:
        print(len(seen) - seen.index(str(l)))
        break
    seen.append(str(l))

    max = (-1, None)
    for i in range(len(l)):
        if l[i] > max[0]:
            max = (l[i], i)
    
    k = max[0] // len(l)
    a = max[0] % len(l)
    index = max[1]

    l[index] = 0

    for i in range(len(l)):
        l[i] += k + int((i - index - 1) % len(l) < a)