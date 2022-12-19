file = open("aoc25_input.txt")
l = file.read().split("\n")
file.close()

key = [int(j) for j in l]

value = 1
sn = -1
ls = 1

while True:
    value *= 7
    value %= 20201227

    for i in range(2):
        if value == key[i]:
            print(value, sn, ls)
            if sn == -1:
                sn = value
            else:
                n = 1
                for j in range(ls):
                    n *= sn
                    n %= 20201227
                print(n)
                exit()
    ls += 1