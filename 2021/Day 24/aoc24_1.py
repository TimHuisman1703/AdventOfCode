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
            r[j], r[i] = 9 - d ,9
        else:
            r[j], r[i] = 9, 9 + d

print(*r, sep="")

# The code above is a formality, in practice I calculated
# the result manually using the following notes:

# z = 0
# z = 2 * z + ((z % 26 + 14) != w) * (25 * z + (w + 12))
# z = 2 * z + ((z % 26 + 15) != w) * (25 * z + (w + 7))
# z = 2 * z + ((z % 26 + 12) != w) * (25 * z + (w + 1))
# z = 2 * z + ((z % 26 + 11) != w) * (25 * z + (w + 2))
# z = 2 * (z // 26) + ((z % 26 - 5) != w) * (25 * (z // 26) + (w + 4))
# z = 2 * z + ((z % 26 + 14) != w) * (25 * z + (w + 15))
# z = 2 * z + ((z % 26 + 15) != w) * (25 * z + (w + 11))
# z = 2 * (z // 26) + ((z % 26 - 13) != w) * (25 * (z // 26) + (w + 5))
# z = 2 * (z // 26) + ((z % 26 - 16) != w) * (25 * (z // 26) + (w + 3))
# z = 2 * (z // 26) + ((z % 26 - 8) != w) * (25 * (z // 26) + (w + 9))
# z = 2 * z + ((z % 26 + 15) != w) * (25 * z + (w + 2))
# z = 2 * (z // 26) + ((z % 26 - 8) != w) * (25 * (z // 26) + (w + 3))
# z = 2 * (z // 26) + ((z % 26 - 0) != w) * (25 * (z // 26) + (w + 3))
# z = 2 * (z // 26) + ((z % 26 - 4) != w) * (25 * (z // 26) + (w + 11))

# 1 <-> 14
# 2 <-> 13
# 3 <-> 10
# 4 <-> 5
# 6 <-> 9
# 7 <-> 8
# 11 <-> 12

# 1 2 3 4 5 6 7 8 9 1011121314
# 1 2 9 9 6 9 9 7 8 2 9 3 9 9

# 12996997829399