file = open("aoc19_input.txt")
l = file.read().split("\n\n")
file.close()

desc = l[0].split("\n")
parts = l[1].split("\n")

rules = {}
for w in desc:
    name, rule = w.split("{")
    rule = rule[:-1].split(",")
    rules[name] = rule

result = 0
for w in parts:
    part = [int(j.split(",")[0]) for j in w[:-1].split("=")[1:]]
    part = {"xmas"[j]: part[j] for j in range(4)}

    curr = "in"
    while True:
        rule = rules[curr]
        next = rule[-1]
        for i in range(len(rule) - 1):
            cnd, dst = rule[i].split(":")

            x = part["x"]
            m = part["m"]
            a = part["a"]
            s = part["s"]
            if eval(cnd):
                next = dst
                break

        if next == "A":
            result += sum(part.values())
            break
        if next == "R":
            break

        curr = next

print(result)