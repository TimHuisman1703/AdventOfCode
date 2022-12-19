file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

def parse(x):
    try:
        return int(x)
    except:
        return reg[x]

reg = {}
sound = 0

for instr in l:
    name = instr.split()[1]

    if name not in reg.keys() and not name.isdecimal():
        reg.update({name: 0})

ip = 0
while ip < len(l):
    command, *args = l[ip].split()

    if command == "snd":
        sound = parse(args[0])
    elif command == "set":
        reg.update({args[0]: parse(args[1])})
    elif command == "add":
        reg.update({args[0]: reg[args[0]] + parse(args[1])})
    elif command == "mul":
        reg.update({args[0]: reg[args[0]] * parse(args[1])})
    elif command == "mod":
        reg.update({args[0]: reg[args[0]] % parse(args[1])})
    elif command == "rcv":
        if parse(args[0]) != 0:
            print(sound)
            break
    elif command == "jgz":
        if parse(args[0]) > 0:
            ip += parse(args[1])
            continue
    
    ip += 1