file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

mask = ""
memIndex = []
memValue = []

for i in l:
	print(i)
	if i[1] == "a":
		mask = i[7:]
	else:
		index = int(i[4:].split("]")[0])
		value = int(i.split(" = ")[1])
		
		address = ""

		for j in range(36):
			if mask[j] == "0":
				address += str((index>>(35-j))&1)
			else:
				address += mask[j]

		c = address.count("X")
		for j in range(1<<c):
			index = address

			for k in range(c):
				index = index.replace("X", str((j>>k)&1), 1)
			
			index = int(index, 2)

			if index not in memIndex:
				memIndex.append(index)
				memValue.append(value)
			else:
				pos = memIndex.index(index)
				memValue[pos] = value

print(sum(memValue))