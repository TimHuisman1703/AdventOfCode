file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

a, b = int(l[0].split()[4]), int(l[1].split()[4])

c = 0
mask = 2**16 - 1
for i in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    
    if a & mask == b & mask:
        c += 1
    
    if i % 1000000 == 999999:
        print(f"Passed {i+1}")

print(c)