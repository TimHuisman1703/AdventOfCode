file = open("aoc01_input.txt")
s = file.read()
file.close()

result = 0
for i in range(len(s)):
	if s[i] == s[(i + 1) % len(s)]:
		result += int(s[i])

print(result)