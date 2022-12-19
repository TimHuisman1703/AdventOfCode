file = open("aoc05_input.txt")
l = file.read().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").split("\n")
file.close()

m = 0
s = []

for i in l:
    s.append(int(i, 2))

s = sorted(s)

print(s)

for i in range(1, len(s)):
    if s[i] != s[i-1]+1:
        print(s[i]-1)