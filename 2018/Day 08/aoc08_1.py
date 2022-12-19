file = open("aoc08_input.txt")
l = [int(j) for j in file.read().split()]
file.close()

stack = [[1, 0]]
index = 0
result = 0

while index < len(l):
    if stack[-1][0] > 0:
        data = l[index:index+2]
        stack[-1][0] -= 1
        stack.append(data)
        index += 2
    else:
        result += sum(l[index:index+stack[-1][1]])
        index += stack[-1][1]
        stack.pop()

print(result)