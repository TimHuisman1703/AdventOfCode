file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

def find_best_strength(bridges, port):
    possible_strengths = [0]
    possible_bridges = filter(lambda x: port in x, bridges)

    for pb in possible_bridges:
        b = bridges.copy()
        b.remove(pb)
        other_port = pb[0] if pb[1] == port else pb[1]
        possible_strengths.append(sum(pb) + find_best_strength(b, other_port))
    
    return max(possible_strengths)

b = [sorted(map(int, j.split("/"))) for j in l]

print(find_best_strength(b, 0))