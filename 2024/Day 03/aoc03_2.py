file = open("aoc03_input.txt")
s = file.read()
file.close()

idx = -1

def mul(x, y):
    return x * y

r = 0
enabled = True
while idx < len(s):
    do_idx = s.find("do()", idx + 1) % (len(s) + 1)
    dont_idx = s.find("don't()", idx + 1) % (len(s) + 1)
    idx = s.find("mul(", idx + 1) % (len(s) + 1)
    if idx == -1:
        break

    if do_idx < idx and do_idx < dont_idx:
        enabled = True
        idx = do_idx
        continue
    if dont_idx < idx:
        enabled = False
        idx = dont_idx
        continue
    
    end = s.find(")", idx)
    if end == -1:
        break
    expr = s[idx:end + 1]

    try:
        if enabled:
            r += eval(expr)
    except:
        pass

print(r)