file = open("aoc03_input.txt")
s = file.read()
file.close()

idx = -1

def mul(x, y):
    return x * y

r = 0
while idx < len(s):
    idx = s.find("mul(", idx + 1)
    if idx == -1:
        break
    
    end = s.find(")", idx)
    if end == -1:
        break
    expr = s[idx:end + 1]

    try:
        r += eval(expr)
    except:
        pass

print(r)