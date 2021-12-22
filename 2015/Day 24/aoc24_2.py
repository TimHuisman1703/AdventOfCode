file = open("aoc24_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

l = l[::-1]
cap = sum(l) // 4

def get_groups(l, i, w):
	if w == 0:
		return [set()]
	if i == len(l) or w < 0:
		return []
	
	included = get_groups(l, i + 1, w - l[i])
	for s in included:
		s.add(l[i])
	excluded = get_groups(l, i + 1, w)
	
	return included + excluded

possible = get_groups(l, 0, cap)
possible = sorted(possible, key=lambda x: len(x))
n = min(len(j) for j in possible)

m = 10**100
for i in range(n):
	p = 1
	for j in possible[i]:
		p *= j
	
	if p < m:
		m = p

print(m)