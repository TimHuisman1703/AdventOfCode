file = open("aoc01_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

print(sum(l))