file = open("aoc05_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

s = 0

for i in l:
	if i.count("a")+i.count("e")+i.count("i")+i.count("o")+i.count("u") > 2:
		if not ("ab" in i or "cd" in i or "pq" in i or "xy" in i):
			for j in range(len(i)-1):
				if i[j] == i[j+1]:
					s += 1
					break

print(s)