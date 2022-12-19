file = open("aoc14_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

time = 2503

speed, stamina, rest = dict(), dict(), dict()
pos, points = [], []

nr = 0
id = dict()

for i in l:
    s = i.split()
    name = s[0]
    speed.setdefault(name, int(s[3]))
    stamina.setdefault(name, int(s[6]))
    rest.setdefault(name, int(s[13]))
    id.setdefault(name, nr)
    pos.append(0)
    points.append(0)
    nr += 1

for i in range(time):
    for name in speed.keys():
        if i % (stamina[name] + rest[name]) < stamina[name]:
            pos[id[name]] += speed[name]
    front = sorted(pos)[-1]
    for j in range(len(pos)):
        if pos[j] == front:
            points[j] += 1
    print(i, points)

print(sorted(points)[-1])