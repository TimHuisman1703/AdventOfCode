file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

def find_longest_bridges(bridges, port):
    queue = [(port, [], bridges)]
    longest_bridges = [[]]

    while queue:
        current_port, current_sequence, available_bridges = queue.pop(0)
        possible_bridges = filter(lambda x: current_port in x, available_bridges)

        if len(current_sequence) == len(longest_bridges[0]):
            longest_bridges.append(current_sequence)
        if len(current_sequence) > len(longest_bridges[0]):
            longest_bridges = [current_sequence]

        for pb in possible_bridges:
            other_port = pb[0] if pb[1] == current_port else pb[1]
            s = current_sequence.copy()
            b = available_bridges.copy()
            s.append(pb)
            b.remove(pb)
            queue.append((other_port, s, b))
    
    return longest_bridges

b = [sorted(map(int, j.split("/"))) for j in l]

longest_bridges = find_longest_bridges(b, 0)

lengths = [sum(sum(j) for j in b) for b in longest_bridges]

print(max(lengths))