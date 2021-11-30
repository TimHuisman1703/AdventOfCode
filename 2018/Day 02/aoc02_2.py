file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

two = 0
three = 0

for i in range(len(l)-1):
	for j in range(i+1, len(l)):
		mistakes = []

		for k in range(len(l[i])):
			if l[i][k] != l[j][k]:
				mistakes.append(k)
				if len(mistakes) > 1:
					break
		
		if len(mistakes) == 1:
			mistake = mistakes[0]
			print(l[i][:mistake] + l[i][mistake+1:])
			exit()