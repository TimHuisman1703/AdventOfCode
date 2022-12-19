file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

two = 0
three = 0

for s in l:
    has_two = False
    has_three = False

    for c in set(s):
        if s.count(c) == 2:
            has_two = True
        if s.count(c) == 3:
            has_three = True
    
    two += has_two
    three += has_three

print(two * three)