file = open("aoc15_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

def outcome(attr, div):
    total = 1
    for i in range(4):
        s = 0
        for j in range(len(attr)):
            s += div[j]*attr[j][i]
        total *= max(0, s)
    return total

attr = []
for i in l:
    s = (i+",").split()
    curr_attr = [int(s[2][:-1]), int(s[4][:-1]), int(s[6][:-1]), int(s[8][:-1]), int(s[10][:-1])]
    attr.append(curr_attr)

m = 0
for i in range(100, -1, -1):
    for j in range(100, -1, -1):
        for k in range(100, -1, -1):
            last = 500 - i*attr[0][4] - j*attr[1][4] - k*attr[2][4]
            if -1 < last < 101 and i+j+k+last == 100:
                result = outcome(attr, [i, j, k, last])
                if result > m:
                    print([i, j, k, last], result, m, attr[0][4]*i+attr[1][4]*j+attr[2][4]*k+last)
                    m = result

print(m)