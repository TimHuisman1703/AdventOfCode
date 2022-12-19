file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

GENERATIONS = 200
GOAL = 50000000000

s = l[0].split()[2]
start = 0

next = {}
for instr in l[2:]:
    args = instr.split(" => ")
    next.update({args[0]: args[1]})

for gen in range(GENERATIONS):
    print(f"{gen}: {s} (Start: {start})")

    s = "...." + s + "...."
    ns = ""

    for i in range(len(s)-4):
        if s[i:i+5] in next.keys():
            ns += next[s[i:i+5]]
        else:
            ns += "."
    
    start += ns.index("#") - 2
    ns = ns[ns.index("#"):len(ns)-ns[::-1].index("#")]
    
    s = ns

print(f"{GENERATIONS}: {s} (Start: {start})")

print(sum(j+(start - GENERATIONS + GOAL) for j in range(len(s)) if s[j] == "#"))