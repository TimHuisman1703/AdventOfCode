file = open("aoc13_input.txt")
l = file.read().split("\n")
file.close()

delay = 0

while True:
    caught = False

    for layer in l:
        r, d = [int(j) for j in layer.split(": ")]

        if (r + delay) % (2*d - 2) == 0:
            caught = True
            break
    
    if not caught:
        print(delay)
        break
    
    delay += 1