file = open("aoc10_input.txt")
l = [0]+[int(j) for j in file.read().split("\n")]
file.close()

l = sorted(l)
l.append(max(l)+3)

print(l)

d = [0]*3

for i in range(1, len(l)):
    d[l[i]-l[i-1]-1] += 1

print(d[0]*d[2])