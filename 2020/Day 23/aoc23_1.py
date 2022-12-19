file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

cups = [int(j) for j in l[0]]

curr_cup = 0
length = len(cups)
turns = 100

for turn in range(turns):
    print(f"Move {turn+1}")
    print(cups)
    
    dest_cup_value = (cups[0] + length - 2) % length + 1

    moved_cups = cups[1:4]
    cups = [cups[0]] + cups[4:]
    
    print(moved_cups)
    
    while dest_cup_value not in cups:
        dest_cup_value = (dest_cup_value + length - 2) % length + 1
    dest_cup = cups.index(dest_cup_value)

    cups = cups[:dest_cup+1] + moved_cups + cups[dest_cup+1:]

    cups = cups[1:] + [cups[0]]

while cups[0] != 1:
    cups = cups[1:] + [cups[0]]

print("Final Result:")
print(cups)
print("".join(str(j) for j in cups[1:]))