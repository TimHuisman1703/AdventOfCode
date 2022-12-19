file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

STEPS = 100

particles = []

for i in range(len(l)):
    attr = [j[3:-1] for j in l[i].split(", ")]
    particles.append(tuple([int(j) for j in a.split(",")] for a in attr))

for _ in range(STEPS):
    slots = {}
    to_be_removed = []
    for p in particles:
        key = str(p[0])
        if key in slots.keys():
            to_be_removed.append(p)
            if slots[key]:
                to_be_removed.append(slots[key])
                slots[key] = None
        else:
            slots[key] = p
    
    for p in to_be_removed:
        particles.remove(p)
    
    for p in particles:
        for degree in range(1, -1, -1):
            for coord in range(3):
                p[degree][coord] += p[degree+1][coord]
    
print(len(particles))