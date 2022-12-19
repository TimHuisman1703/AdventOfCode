file = open("aoc21_input.txt")
code = file.read().split("\n")
file.close()

fs = set()
last = 0
f = 0

while 1:
    e = f | 65536
    f = 15466939

    while 1:
        f = ((f + (e & 255)) * 65899) & 16777215

        if e < 256:
            if f not in fs:
                last = f
                fs.add(f)
                break
            else:
                print(last)
                exit()
        else:
            e //= 256