file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

CARDS = 10007

pos = 2019
for _ in range(2):
    for i in l:
        if i.startswith("deal into"):
            pos = CARDS - 1 - pos
        elif i.startswith("cut"):
            a = int(i.split()[-1])
            pos = (pos - a) % CARDS
        else:
            a = int(i.split()[-1])
            pos = (pos * a) % CARDS

print(pos)