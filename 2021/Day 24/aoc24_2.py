file = open("aoc24_input.txt")
code = file.read().split("\n")
file.close()

r = [0 for _ in range(14)]

stack = []
for i in range(14):
    if code[18 * i + 4] == "div z 1":
        a = int(code[18 * i + 15].split()[-1])
        stack.append((i, a))
    else:
        a = int(code[18 * i + 5].split()[-1])
        j, b = stack.pop()

        d = a + b
        if d > 0:
            r[j], r[i] = 1, 1 + d
        else:
            r[j], r[i] = 1 - d, 1

print(*r, sep="")

# The code above is a formality, in practice I calculated
# the result manually using the following notes:

# 1 <-> 14
# 2 <-> 13
# 3 <-> 10
# 4 <-> 5
# 6 <-> 9
# 7 <-> 8
# 11 <-> 12

# 1 2 3 4 5 6 7 8 9 1011121314
# 1 2 9 9 6 9 9 7 8 2 9 3 9 9
# 1 1 8 4 1 2 3 1 1 1 7 1 8 9

# 11841231117189