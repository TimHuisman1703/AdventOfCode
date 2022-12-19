file = open("aoc09_input.txt")
s = file.read()
file.close()

i = 0
height = 0
in_garbage = False
count = 0

while i < len(s):
    c = s[i]

    if c == "!":
        i += 1
    elif c == "<" and not in_garbage:
        in_garbage = True
    elif c == ">":
        in_garbage = False
    elif c == "{" and not in_garbage:
        height += 1
    elif c == "}" and not in_garbage:
        height -= 1
    elif in_garbage:
        count += 1
    
    i += 1

print(count)