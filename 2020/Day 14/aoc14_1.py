file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

mask = ""
memIndex = []
memValue = []

for i in l:
	if i[1] == "a":
		mask = i[7:]
	else:
		index = int(i[4:].split("]")[0])
		value = int(i.split(" = ")[1])

		for j in range(36):
			if mask[35-j] == "1":
				value |= 1<<j
			if mask[35-j] == "0":
				value &= (1<<36)-1-(1<<j)

		if index not in memIndex:
			memIndex.append(index)
			memValue.append(value)
		else:
			pos = memIndex.index(index)
			memValue[pos] = value
		print(f"mem[{index}] = {value}")

print(sum(memValue))