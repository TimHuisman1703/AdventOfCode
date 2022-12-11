file = open("aoc11_input.txt")
l = file.read().split("\n")
file.close()

n = l.count("") + 1

has = []
operations = []
div = []

for i in range(0, len(l) + 1, 7):
    has.append([int(j) for j in l[i + 1][len("  Starting items: "):].split(", ")])
    operations.append(l[i + 2][len("  Operation: "):])
    d = int(l[i + 3].split()[-1])
    t = int(l[i + 4].split()[-1])
    f = int(l[i + 5].split()[-1])
    div.append((d, t, f))

new = -1
checked = [0] * n

for _ in range(20):
    for j in range(n):
        for old in has[j]:
            checked[j] += 1
            exec(operations[j])
            new = new // 3
            if new % div[j][0] == 0:
                has[div[j][1]].append(new)
            else:
                has[div[j][2]].append(new)
        has[j] = []

checked = sorted(checked)
print(checked[-2] * checked[-1])