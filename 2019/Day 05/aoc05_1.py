file = open("aoc05_input.txt")
code = [int(j) for j in file.read().split(",")]
file.close()

ip = 0

while ip < len(code):
    op = code[ip]

    if op % 100 == 1:        # 1:     Addition
        a, b, dst = code[ip+1:ip+4]
        if op // 100 % 10 == 0:
            a = code[a]
        if op // 1000 % 10 == 0:
            b = code[b]
        code[dst] = a + b
        ip += 4
    elif op % 100 == 2:        # 2:    Multiplication
        a, b, dst = code[ip+1:ip+4]
        if op // 100 % 10 == 0:
            a = code[a]
        if op // 1000 % 10 == 0:
            b = code[b]
        code[dst] = a * b
        ip += 4
    elif op % 100 == 3:        # 3:    Input
        dst = code[ip+1]
        code[dst] = 1
        ip += 2
    elif op % 100 == 4:        # 4:    Output
        src = code[ip+1]
        if op // 100 % 10 == 0:
            src = code[src]
        print(src, end=" ")
        ip += 2
    elif op % 100 == 99:    # 99:    Exit
        break