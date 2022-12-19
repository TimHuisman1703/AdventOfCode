file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

d = {}

all_food = set()
amount = {}

for i in l:
    s = i.split(" (contains ")
    food = set(s[0].split())
    allergens = s[1][:-1].split(", ")

    all_food |= food

    for j in food:
        if j in amount:
            amount.update({j: amount[j]+1})
        else:
            amount.setdefault(j, 1)

    for j in allergens:
        if j in d.keys():
            n = d[j] & food
            d.update({j: n})
        else:
            d.setdefault(j, food)

print(d)

all_allergic = set()

for i in d.values():
    all_allergic |= i

non_allergic = all_food - all_allergic

c = 0

for i in non_allergic:
    c += amount[i]

print(c)