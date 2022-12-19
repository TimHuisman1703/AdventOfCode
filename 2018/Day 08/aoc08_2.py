file = open("aoc08_input.txt")
l = [int(j) for j in file.read().split()]
file.close()

stack = [[1, 0, []]]
index = 0

while index < len(l):
    if stack[-1][0] > 0:
        data = l[index:index+2] + [[]]
        if data[0] == 0:
            data[0] = -1
        
        stack[-1][0] -= 1
        stack.append(data)
        index += 2
    else:
        points = 0
        if stack[-1][0] == -1:
            points = sum(l[index:index+stack[-1][1]])
        else:
            for i in l[index:index+stack[-1][1]]:
                if i-1 > -1 and i-1 < len(stack[-1][2]):
                    points += stack[-1][2][i-1]
        
        index += stack[-1][1]
        stack.pop()
        stack[-1][2].append(points)

print(stack[0][2][0])