file = open("aoc16_input.txt")
l = file.read().split(",")
file.close()

s = "abcdefghijklmnop"
def dance(s):
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
    
    return s

i = 0
while True:
    s = dance(s)
    i += 1

    if s == "abcdefghijklmnop":
        for i in range(1000000000 % i):
            s = dance(s)
        print(s)
        break