file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

import gurobipy as gp

r = 0
for idx, row in enumerate(l):
    _, *ps, ts = row.split()

    ts = tuple(int(j) for j in ts[1:-1].split(","))
    ps = [tuple([int(j) for j in p[1:-1].split(",")]) for p in ps]

    with gp.Env(empty=True) as env:
        env.setParam("OutputFlag", 0)
        env.start()

        with gp.Model(env=env) as model:
            xs = [model.addVar(vtype=gp.GRB.INTEGER, name=f"x{j}") for j in range(len(ps))]

            for i, x in enumerate(xs):
                model.addConstr(x >= 0)

            contains = [[] for _ in range(len(ts))]
            for i, p in enumerate(ps):
                for x in p:
                    contains[x].append(i)
            for t, con in zip(ts, contains):
                model.addConstr(sum(xs[j] for j in con) == t)

            model.setObjective(sum(xs), gp.GRB.MINIMIZE)
            model.optimize()

            r += sum(round(x.x) for x in xs)

print(r)