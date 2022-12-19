file = open("aoc14_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

time = 2503

speed, stamina, rest = dict(), dict(), dict()

for i in l:
    s = i.split()
    name = s[0]
    speed.setdefault(name, int(s[3]))
    stamina.setdefault(name, int(s[6]))
    rest.setdefault(name, int(s[13]))

pos = dict()
for i in speed.keys():
    pos.setdefault(i, (time // (stamina[i] + rest[i])) * stamina[i] * speed[i] + min(time % (stamina[i] + rest[i]), stamina[i]) * speed[i])

print(sorted(pos.values())[-1])