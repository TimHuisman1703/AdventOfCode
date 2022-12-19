file = open("aoc04_input.txt")
a, b = [int(j) for j in file.read().split("-")]
file.close()

c = 0
for i in range(a, b+1):
    double = False
    ascending = True

    last = i % 10
    while i > 9:
        i //= 10
        curr = i % 10

        if curr > last:
            ascending = False
            break
        if last == curr:
            double = True

        last = curr
    
    if double and ascending:
        c += 1

print(c)