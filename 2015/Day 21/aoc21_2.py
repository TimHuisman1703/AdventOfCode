file = open("aoc20_input.txt")
p = int(file.read())
file.close()

p //= 11
d = {1: 1}

i = 1
while d[i] < p:
	n = 49
	j = i
	while n:
		n -= 1
		j += i
		try:
			d[j] += i
		except:
			d[j] = i + j
	
	i += 1
	try:
		d[i]
	except:
		d[i] = 0

print(i)