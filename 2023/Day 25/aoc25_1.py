file = open("aoc25_input.txt")
l = file.read().split("\n")
file.close()

from scipy.sparse import *
import random

neighbors = {}

for w in l:
    a, bs = w.split(": ")

    for b in bs.split():
        neighbors[a] = neighbors.get(a, [])
        neighbors[a].append(b)
        neighbors[b] = neighbors.get(b, [])
        neighbors[b].append(a)

keys = [*neighbors.keys()]
n = len(keys)

matrix = [[int(b in neighbors[a]) for b in keys] for a in keys]
graph = csr_matrix(matrix)

flow = 0
while flow != 3:
    s = random.randrange(0, n)
    t = random.randrange(0, n)
    if s == t:
        continue

    result = csgraph.maximum_flow(graph, s, t)
    flow = result.flow_value

source_nodes = csgraph.depth_first_order(graph - result.flow, s)[0]
k = len(source_nodes)

print(k * (n - k))