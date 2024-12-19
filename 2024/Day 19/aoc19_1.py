file = open("aoc19_input.txt")
l = file.read().split("\n")
file.close()

ps = set(l[0].split(", "))

r = 0
for w in l[2:]:
    pos = [False] * (len(w) + 1)
    pos[0] = True

    for i in range(1, len(w) + 1):
        for j in range(i):
            if pos[j]:
                if w[j:i] in ps:
                    pos[i] = True
                    break

    r += pos[-1]

print(r)