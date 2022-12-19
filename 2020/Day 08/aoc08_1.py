file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

s = set()
ip = 0
acc = 0
while ip not in s:
    s.add(ip)
    print(str(ip) + ": " + l[ip] + " (" + str(acc) + ")")
    if l[ip][:3] == "jmp":
        ip += int(l[ip][4:])
    else:
        if l[ip][:3] == "acc":
            acc += int(l[ip][4:])
        ip += 1

print(str(ip) + ": Already Visited")
print(acc)