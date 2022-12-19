file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

for i in range(len(l)):
    s = set()
    ip = 0
    acc = 0
    correct = False
    while ip not in s:
        if ip == len(l):
            correct = True
            break

        s.add(ip)
        print(str(ip) + ": " + l[ip] + " (" + str(acc) + ")")
        if(ip != i and l[ip][:3] == "jmp") or (ip == i and l[ip][:3] == "nop"):
            ip += int(l[ip][4:])
        else:
            if l[ip][:3] == "acc":
                acc += int(l[ip][4:])
            ip += 1
    
    if correct:
        print(acc)
        exit()