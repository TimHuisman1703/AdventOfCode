file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

limits = []

def merge_region(start, end):
    global limits

    limits.append((start, end))
    limits = sorted(limits, key=lambda x: x[0])

    i = 0
    while i < len(limits)-1:
        if limits[i][1] >= limits[i+1][0]-1:
            new_start = limits[i][0]
            new_end = max(limits[i][1], limits[i+1][1])
            limits = limits[:i] + limits[i+2:] + [(new_start, new_end)]
            limits = sorted(limits, key=lambda x: x[0])
        else:
            i += 1

for s in l:
    start, end = [int(j) for j in s.split("-")]
    merge_region(start, end)

print(limits[0][1]+1)