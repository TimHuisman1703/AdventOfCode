file = open("aoc08_input.txt")
s = file.read()
file.close()

WIDTH = 25
HEIGHT = 6

n = WIDTH * HEIGHT
l = [s[j:j+n] for j in range(0, len(s), n)]
m = min(l, key=lambda x: x.count("0"))

print(m.count("1") * m.count("2"))