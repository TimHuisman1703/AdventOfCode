file = open("aoc01_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

for i in l:
    if(i == 1010):
        continue
    if(l.count(2020-i) > 0):
        print(i, 2020-i)
        print(i*(2020-i))
        exit(0)