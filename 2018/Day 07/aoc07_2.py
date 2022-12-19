file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

STEP_OFFSET = 60
WORKERS = 5

req = {}

queue = []
in_progress = []
done = []

for instr in l:
    args = instr.split()

    if args[1] not in req.keys():
        req.update({args[1]: []})
    if args[7] not in req.keys():
        req.update({args[7]: []})
    
    req[args[7]].append(args[1])

minute = 0
while req or queue or in_progress:
    newly_done = []
    for c, progress in in_progress:
        if progress == 0:
            newly_done.append(c)
    for c in newly_done:
        in_progress.remove((c, 0))
        done.append(c)

    possible = [j for j in sorted(req.keys())]
    
    for c in possible:
        if all(j in done for j in req[c]):
            queue.append(c)
            req.pop(c)

    while len(in_progress) < WORKERS and queue:
        c = queue.pop(0)
        in_progress.append((c, ord(c) - 64 + STEP_OFFSET))
    
    in_progress = [(j[0], j[1]-1) for j in in_progress]
    
    minute += 1

print(minute-1)