file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

root = "ahnofa"
children = {}
own_weights = {}
weights = {}

for s in l:
	args = s.replace(",", "").split()
	own_weight = int(args[1][1:-1])

	children.update({args[0]: args[3:]})
	own_weights.update({args[0]: own_weight})

def get_weight(node):
	global weights

	if node in weights.keys():
		return weights[node]
	
	weight = own_weights[node]
	for child in children[node]:
		weight += get_weight(child)
	
	weights.update({node: weight})
	return weight

get_weight(root)

def inspect(node, definitely_here):
	c = children[node]
	w = [weights[j] for j in c]

	if len(c) > 1 and weights[c[0]] * len(c) == sum(w):
		if definitely_here:
			return [node]
		
		return []
	
	result = []
	for i in c:
		if w.count(weights[i]) == 1:
			result += inspect(i, len(c) > 2)
	return result

wrong_node = inspect(root, False)[0]

parent = None
for p, c in children.items():
	if wrong_node in c:
		parent = p

actual_weight = weights[wrong_node]
sibling_weights = [weights[c] for c in children[parent]]
desired_weight = sorted(sibling_weights, key=lambda x: -sibling_weights.count(x))[0]

print(own_weights[wrong_node] + desired_weight - actual_weight)