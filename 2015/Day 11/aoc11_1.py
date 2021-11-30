file = open("aoc11_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

def update_list(l):
	i = len(l)-1
	while l[i] == 25:
		l[i] = 0
		i -= 1
		if i == -1:
			return l
	l[i] += 1
	return l

n = update_list([ord(j)-97 for j in l[0]])
while True:
	if not(8 in n or 11 in n or 14 in n):
		for i in range(len(n)-2):
			if n[i+1] == n[i]+1 and n[i+2] == n[i]+2:
				r = 0
				j = 0
				while j < len(n)-1:
					if n[j] == n[j+1]:
						r += 1
						j += 1
					j += 1
				if r > 1:
					print("".join(chr(k+97) for k in n))
					exit()
				break
	n = update_list(n)