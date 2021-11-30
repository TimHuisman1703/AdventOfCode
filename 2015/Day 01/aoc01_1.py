file = open("aoc01_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

print(l[0].count("(")-l[0].count(")"))