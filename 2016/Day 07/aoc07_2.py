def get_abas(s):
	abas = []

	for i in range(len(s)-2):
		if s[i] != s[i+1] and s[i] == s[i+2]:
			abas.append(s[i:i+3])

	return abas

file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

c = 0

for ip in l:
	out_abas = []
	in_abas = []

	while "]" in ip:
		index = ip.index("]")
		segment, ip = ip[:index], ip[index+1:]

		out_segment, in_segment = segment.split("[")
		
		out_abas += get_abas(out_segment)
		in_abas += get_abas(in_segment)
	
	out_abas += get_abas(ip)
	
	valid = False
	for aba in out_abas:
		bab = aba[1:] + aba[1]

		if bab in in_abas:
			valid = True
	
	if valid:
		c += 1

print(c)