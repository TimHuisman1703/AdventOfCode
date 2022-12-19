file = open("aoc01_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

for i in l:
    for j in l:
        if(i == j):
            continue
        if(i == 2020-j-i):
            continue
        if(j == 2020-i-j):
            continue
        if(l.count(2020-i-j) > 0):
            print(i, j, 2020-i-j)
            print(i*j*(2020-i-j))
            exit(0)