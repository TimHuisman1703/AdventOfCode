file = open("aoc17_input.txt")
s = int(file.read())
file.close()

l = [0]

for i in range(1, 2018):
    rotation = s % i
    l = l[rotation:] + l[:rotation] + [i]

print(l[0])