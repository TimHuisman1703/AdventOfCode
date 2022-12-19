file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

x = int(l[0].split()[4])
y = int(l[1].split()[4])

mem = {}
def opt(a, b, x, y, turn):
    key = (a, b, x, y, turn)
    if key in mem.keys():
        return mem[key]
    
    if a <= 0:
        mem[key] = (1, 0)
        return (1, 0)
    if b <= 0:
        mem[key] = (0, 1)
        return (0, 1)

    wa, wb = 0, 0
    
    for die_a in range(1, 4):
        for die_b in range(1, 4):
            for die_c in range(1, 4):
                t = die_a + die_b + die_c
                if turn == 0:
                    nx = (x - 1 + t) % 10 + 1
                    da, db = opt(a - nx, b, nx, y, 1 - turn)
                else:
                    ny = (y - 1 + t) % 10 + 1
                    da, db = opt(a, b - ny, x, ny, 1 - turn)
                wa, wb = wa + da, wb + db
    
    mem[key] = (wa, wb)
    return mem[key]

wa, wb = opt(21, 21, x, y, 0)
print(max(wa, wb))