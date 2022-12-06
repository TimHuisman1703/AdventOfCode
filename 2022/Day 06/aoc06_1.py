file = open("aoc06_input.txt")
s = file.read()
file.close()

i = 4
while len(set([*s[i-4:i]])) < 4:
    i += 1

print(i)