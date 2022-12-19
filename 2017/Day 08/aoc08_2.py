file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

reg = {}
for instr in l:
    name = instr.split()[0]
    reg.update({name: 0})

highest = 0

for instr in l:
    args = instr.split()
    
    args[4] = f"reg[\"{args[4]}\"]"
    cond = " ".join(args[4:])

    if eval(cond):
        value = int(args[2]) * (1 - 2 * int(args[1] == "dec"))
        reg.update({args[0]: reg[args[0]] + value})
    
    highest = max(highest, max(reg.values()))

print(highest)