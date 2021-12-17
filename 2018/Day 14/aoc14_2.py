file = open("aoc14_input.txt")
seq = [int(j) for j in file.read()]
file.close()

class Node:
	def __init__(self, value, id, prev=None, next=None):
		self.value = value
		self.id = id

		if prev and next:
			self.prev = prev
			self.next = next
		else:
			self.prev = self
			self.next = self
	
	def set_next(self, node):
		node.prev = self
		node.next = self.next
		self.next.prev = node
		self.next = node

size = 2
head = a = Node(3, 0)
b = Node(7, 1)
a.set_next(b)
p = head

while 1:
	i, j = a.value, b.value
	r = i + j

	if r < 10:
		head.prev.set_next(Node(r, size))
		size += 1
	else:
		head.prev.set_next(Node(1, size))
		head.prev.set_next(Node(r % 10, size + 1))
		size += 2
	
	while i + 1:
		a = a.next
		i -= 1
	while j + 1:
		b = b.next
		j -= 1
	
	while p.id <= size - len(seq):
		if p.id % 100000 == 0:
			print("Current ID:", p.id)
		curr = p
		for i in range(len(seq)):
			if curr.value != seq[i]:
				break
			curr = curr.next
		else:
			print(p.id)
			exit()
		p = p.next