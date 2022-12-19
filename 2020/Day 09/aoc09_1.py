file = open("aoc09_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

p = 25
r = []

for i in range(p, len(l)):
    for j in range(i-p, i):
        if l[i] == 2*l[j]:
            continue

        if l[i-p:i].count(l[i]-l[j]):
            print(i, l[i], l[j], l[i]-l[j])
            r.append(i)
            break

for i in range(1, len(r)):
    if r[i] != r[i-1]+1:
        print(i+25, l[i+25])