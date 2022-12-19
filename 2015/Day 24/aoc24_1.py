file = open("aoc24_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

l = l[::-1]
cap = sum(l) // 3

def get_group(l, i, w, n):
    if w == 0:
        return True, []
    if i >= len(l) or w < 0 or n == 0:
        return False, []
    
    success, s = get_group(l, i + 1, w - l[i], n - 1)
    if success:
        return success, [l[i]] + s
    
    success, s = get_group(l, i + 1, w, n)
    return success, s

n = 0
success = False
while not success:
    n += 1
    success, s = get_group(l, 0, cap, n)

p = 1
for i in s:
    p *= i

print(p)