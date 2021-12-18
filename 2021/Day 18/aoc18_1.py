file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

size = 0

class Node:
	def __init__(self, value):
		global size
		self.num = size
		size += 1

		self.value = value
		self.parent = None
		self.left = None
		self.right = None

def parse_node(s):
	global size

	if s[0] != "[":
		return Node(int(s[0]))
	
	parent = Node(-1)
	
	if s[1] == "[":
		comma = find_pair(s, 1) + 1
	else:
		comma = 2
	left = parse_node(s[1:comma])
	right = parse_node(s[comma+1:-1])

	left.parent = parent
	parent.left = left
	right.parent = parent
	parent.right = right
	
	return parent

def to_string(n, with_num=False):
	if n.value != -1:
		return str(n.value) if not with_num else str(n.num)
	
	return "[" + to_string(n.left, with_num) + "," + to_string(n.right, with_num) + "]"

def find_pair(s, i):
	h = 1
	while h:
		i += 1
		if s[i] == "[":
			h += 1
		elif s[i] == "]":
			h -= 1
	return i

def magnitude(n):
	if n.value != -1:
		return n.value
	
	return 3 * magnitude(n.left) + 2 * magnitude(n.right)

root = parse_node(l[0])

for i in range(1, len(l)):
	to_add = parse_node(l[i])

	new_root = Node(-1)
	new_root.left = root
	root.parent = new_root
	new_root.right = to_add
	to_add.parent = new_root
	root = new_root

	# DFS
	split_list = []
	changed = True
	while changed:
		changed = False

		depth = 0
		visited = set([None])
		curr = root

		# Exploding DFS
		while 1:
			if depth >= 4 and curr.value == -1 and curr.left.value != -1 and curr.right.value != -1:
				changed = True

				a, b = curr.left.value, curr.right.value

				zero_node = Node(0)
				zero_node.parent = curr.parent
				if curr.parent.left == curr:
					curr.parent.left = zero_node
				else:
					curr.parent.right = zero_node

				# Find left node and add
				curr_neighbor = zero_node
				while curr_neighbor.parent and curr_neighbor.parent.left == curr_neighbor:
					curr_neighbor = curr_neighbor.parent
				
				if curr_neighbor.parent:
					curr_neighbor = curr_neighbor.parent.left
					while curr_neighbor.value == -1:
						curr_neighbor = curr_neighbor.right
					curr_neighbor.value += a

					# If too much, split
					if curr_neighbor.value > 9:
						if curr_neighbor not in split_list:
							split_list.append(curr_neighbor)

				# Find right node and add
				curr_neighbor = zero_node
				while curr_neighbor.parent and curr_neighbor.parent.right == curr_neighbor:
					curr_neighbor = curr_neighbor.parent
				
				if curr_neighbor.parent:
					curr_neighbor = curr_neighbor.parent.right
					while curr_neighbor.value == -1:
						curr_neighbor = curr_neighbor.left
					curr_neighbor.value += b

					# If too much, split
					if curr_neighbor.value > 9:
						if curr_neighbor not in split_list:
							split_list.append(curr_neighbor)
				
				# Start from the beginning
				depth = 0
				visited = set([None])
				curr = root
				
				continue

			if curr in visited and curr.left in visited and curr.right in visited:
				depth -= 1
				if curr.parent:
					curr = curr.parent
				else:
					break
			
			visited.add(curr)

			if curr.left and curr.left not in visited:
				depth += 1
				curr = curr.left
			elif curr.right and curr.right not in visited:
				depth += 1
				curr = curr.right

		# Splitting DFS
		depth = 0
		visited = set([None])
		curr = root

		# Exploding DFS
		while 1:
			if curr.value > 9:
				changed = True
				
				c, d = curr.value // 2, (curr.value + 1) // 2
				split_left = Node(c)
				split_right = Node(d)
				split_parent = Node(-1)
				split_parent.parent = curr.parent
				split_parent.left = split_left
				split_parent.right = split_right
				
				if curr.parent.left == curr:
					curr.parent.left = split_parent
				else:
					curr.parent.right = split_parent
				split_left.parent = split_parent
				split_right.parent = split_parent

				break

			if curr in visited and curr.left in visited and curr.right in visited:
				depth -= 1
				if curr.parent:
					curr = curr.parent
				else:
					break
			
			visited.add(curr)

			if curr.left and curr.left not in visited:
				depth += 1
				curr = curr.left
			elif curr.right and curr.right not in visited:
				depth += 1
				curr = curr.right

print(magnitude(root))