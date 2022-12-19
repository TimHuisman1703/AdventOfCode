file = open("aoc12_input.txt")
code = file.read().split("\n")
file.close()

ip = 0
reg = {"a": 0, "b": 0, "c": 1, "d": 0}

while ip < len(code):
    args = code[ip].split()

    if args[0] == "cpy":
        value = reg[args[1]] if args[1] in "abcd" else int(args[1])
        reg.update({args[2]: value})
        ip += 1
    elif args[0] == "inc":
        reg.update({args[1]: reg[args[1]] + 1})
        ip += 1
    elif args[0] == "dec":
        reg.update({args[1]: reg[args[1]] - 1})
        ip += 1
    elif args[0] == "jnz":
        value = reg[args[1]] if args[1] in "abcd" else int(args[1])
        if value != 0:
            ip += int(args[2])
        else:
            ip += 1

for r in sorted(reg.keys()):
    print(f"{r} = {reg[r]}")