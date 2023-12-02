file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

s = 0
for i in range(len(l)):
    b = l[i].split(": ")[1].split("; ")
    min_count = {"red": 0, "green": 0, "blue": 0}

    for g in b:
        count = {}
        for w in g.split(", "):
            n, t = w.split()
            count[t] = count.get(t, 0) + int(n)

        min_count["red"] = max(min_count["red"], count.get("red", 0))
        min_count["green"] = max(min_count["green"], count.get("green", 0))
        min_count["blue"] = max(min_count["blue"], count.get("blue", 0))

    s += min_count["red"] * min_count["green"] * min_count["blue"]

print(s)