file = open("aoc23_input.txt")
code = file.read().split("\n")
file.close()

ip = 0
reg = {"a": 7, "b": 0, "c": 0, "d": 0}

toggle_op_codes = {
    "inc": "dec",
    "dec": "inc",
    "tgl": "inc",
    "jnz": "cpy",
    "cpy": "jnz"
}

def parse(reg_or_imm):
    return reg[reg_or_imm] if reg_or_imm in "abcd" else int(reg_or_imm)

while ip < len(code):
    args = code[ip].split()
    
    if args[0] == "inc":
        reg.update({args[1]: reg[args[1]] + 1})
        ip += 1
    elif args[0] == "dec":
        reg.update({args[1]: reg[args[1]] - 1})
        ip += 1
    elif args[0] == "tgl":
        try:
            index = ip + parse(args[1])
            tgl_args = code[index].split()
            tgl_args[0] = toggle_op_codes[tgl_args[0]]
            new_command = " ".join(tgl_args)
            code[index] = new_command
        except:
            pass
        ip += 1
    elif args[0] == "cpy":
        if args[2] in "abcd":
            reg.update({args[2]: parse(args[1])})
        ip += 1
    elif args[0] == "jnz":
        if parse(args[1]) != 0:
            ip += int(parse(args[2]))
        else:
            ip += 1

for r in sorted(reg.keys()):
    print(f"{r} = {reg[r]}")