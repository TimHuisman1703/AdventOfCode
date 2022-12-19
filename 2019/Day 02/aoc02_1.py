file = open("aoc02_input.txt")
code = [int(j) for j in file.read().split(",")]
file.close()

ip = 0

code[1] = 12
code[2] = 2

while ip < len(code):
    if code[ip] == 1:
        args = code[ip+1:ip+4]
        code[args[2]] = code[args[0]] + code[args[1]]
        ip += 4
        continue
    
    if code[ip] == 2:
        args = code[ip+1:ip+4]
        code[args[2]] = code[args[0]] * code[args[1]]
        ip += 4
        continue
    
    if code[ip] == 99:
        break

print(code[0])