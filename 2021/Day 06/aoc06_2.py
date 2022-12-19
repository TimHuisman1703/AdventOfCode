file = open("aoc06_input.txt")
l = [int(j) for j in file.read().split(",")]
file.close()

N = 256

mem = [[-1 for left in range(N + 1)] for timer in range(9)]

def get_children(timer, left):
    global mem

    if left == 0:
        return 1
    
    if mem[timer][left] > -1:
        return mem[timer][left]
    
    result = 0
    if timer > 0:
        result = get_children(timer - 1, left - 1)
    else:
        result += get_children(6, left - 1) + get_children(8, left - 1)
    
    mem[timer][left] = result
    return result

print(sum(get_children(j, N) for j in l))