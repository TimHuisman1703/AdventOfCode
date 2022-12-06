file = open("aoc06_input.txt")
s = file.read()
file.close()

i = 14
while len(set([*s[i-14:i]])) < 14:
    i += 1

print(i)