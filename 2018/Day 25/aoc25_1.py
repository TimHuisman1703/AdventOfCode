file = open("aoc25_input.txt")
l = file.read().split("\n")
file.close()

class UnionFind:
	def __init__(self, n):
		self.parent = [j for j in range(n)]
		self.rank = [0] * n
	
	def find(self, x):
		return x if x == self.parent[x] else self.find(self.parent[x])
	
	def join(self, x, y):
		a = self.find(x)
		b = self.find(y)

		if a == b:
			return False
		
		if self.rank[a] >= self.rank[b]:
			self.parent[b] = a
			if self.rank[a] == self.rank[b]:
				self.rank[a] += 1
		else:
			self.parent[a] = b
		
		return True

s = []
for i in l:
	s.append(tuple([int(j) for j in i.split(",")]))

c = len(s)
uf = UnionFind(c)

for i in range(len(s) - 1):
	for j in range(i + 1, len(s)):
		if sum(abs(s[i][k] - s[j][k]) for k in range(4)) <= 3:
			if uf.join(i, j):
				c -= 1

print(c)