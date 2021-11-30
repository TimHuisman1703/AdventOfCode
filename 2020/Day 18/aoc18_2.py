file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

def add_parentheses(s):
	s = s.replace(" ", "")
	for i in range(len(s))[::-1]:
		if s[i] == "+":
			start = i-1
			end = i+1
			c = 0
			while start > -1 and (s[start].isdigit() or s[start] == ")" or c > 0):
				start -= 1
				if start == -1:
					break
				if s[start] == ")":
					c += 1
				elif s[start] == "(":
					c -= 1
			c = 0
			while end < len(s) and (s[end].isdigit() or s[end] == "(" or c > 0):
				end += 1
				if end == len(s):
					break
				if s[end] == "(":
					c += 1
				elif s[end] == ")":
					c -= 1
			s = s[:start+1] + "(" + s[start+1:end] + ")" + s[end:]
	return s

print(sum(eval(add_parentheses(j)) for j in l))