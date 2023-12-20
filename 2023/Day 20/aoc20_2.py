file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

from collections import deque
from math import lcm

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

result = 0
vs = {}
while True:
    q = deque([(x, "roadcaster", False) for x in initial])
    result += 1

    done = False
    while q:
        curr, fr, is_high = q.popleft()

        if curr in pred["rx"] and is_high:
            if fr not in vs:
                vs[fr] = result

            if len(vs) == len(pred[curr]):
                done = True
                break

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

    if done:
        break

p = 1
for v in vs.values():
    p = lcm(p, v)

print(p)