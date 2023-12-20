file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

from collections import deque

low = 0
high = 0

initial = []
state = {}
pred = {}
succ = {}
for w in l:
    src, dst = w.split(" -> ")
    dsts = dst.split(", ")

    if src[0] == "b":
        initial = dsts
    if src[0] == "%":
        state[src[1:]] = (0, [False])
    if src[0] == "&":
        state[src[1:]] = (1, {})

    succ[src[1:]] = dsts
    for dst in dsts:
        pred[dst] = pred.get(dst, set()) | set([src[1:]])

for x in state:
    if state[x][0] == 1:
        for s in pred[x]:
            state[x][1][s] = False

for _ in range(1000):
    q = deque([(x, "roadcaster", False) for x in initial])
    low += 1

    while q:
        curr, fr, is_high = q.popleft()

        if is_high:
            high += 1
        else:
            low += 1

        if curr not in state:
            continue

        if state[curr][0] == 0 and is_high:
            continue

        send_high = False
        if state[curr][0] == 0:
            state[curr][1][0] = not state[curr][1][0]
            if state[curr][1][0]:
                send_high = True
        if state[curr][0] == 1:
            state[curr][1][fr] = is_high
            if not all(state[curr][1].values()):
                send_high = True

        for to in succ[curr]:
            q.append((to, curr, send_high))

print(high * low)