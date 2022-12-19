file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

result = 0
for row in l:
    words = ["".join(sorted(j)) for j in row.split()]
    if len(set(words)) == len(words):
        result += 1

print(result)