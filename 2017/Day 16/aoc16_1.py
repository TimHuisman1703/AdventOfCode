file = open("aoc16_input.txt")
l = file.read().split(",")
file.close()

s = "abcdefghijklmnop"

for instr in l:
    command, args = instr[0], instr[1:].split("/")

    if command == "s":
        x = -int(args[0])
        s = s[x:] + s[:x]
    elif command == "x":
        a, b = sorted(int(j) for j in args)
        s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    elif command == "p":
        a, b = args
        s = s.replace(a, "X").replace(b, a).replace("X", b)

print(s)