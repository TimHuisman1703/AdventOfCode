file = open("aoc13_input.txt")
l = file.read().split("\n")
file.close()

severity = 0
for layer in l:
    r, d = [int(j) for j in layer.split(": ")]

    if r % (2*d - 2) == 0:
        severity += r*d

print(severity)