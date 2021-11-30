file = open("aoc10_input.txt")
l = [0]+[int(j) for j in file.read().split("\n")]
file.close()

l = sorted(l)
l.append(max(l)+3)

print(l)

w = [0]*len(l)
w[0] = 1

for i in range(1, len(l)):
	for j in range(1, 4):
		if i-j > -1 and l[i-j] < l[i] <= l[i-j]+3:
			w[i] += w[i-j]

print(w)
print(w[len(w)-1])