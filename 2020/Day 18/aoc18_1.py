file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

def evaluate(s):
    if s.isdigit():
        return int(s)
    
    for i in range(len(s))[::-1]:
        if s[i].isdigit():
            continue
        if s[i] == "+":
            return int(s[i+1:]) + evaluate(s[:i])
        if s[i] == "*":
            return int(s[i+1:]) * evaluate(s[:i])
        if s[i] == ")":
            c = 1
            while c:
                i -= 1
                if s[i] == ")":
                    c += 1
                elif s[i] == "(":
                    c -= 1
            i -= 1
            if s[i] == "+":
                return evaluate(s[i+2:-1]) + evaluate(s[:i])
            if s[i] == "*":
                return evaluate(s[i+2:-1]) * evaluate(s[:i])
            if i == -1:
                return evaluate(s[1:-1])

print(sum(evaluate(j.replace(" ", "")) for j in l))