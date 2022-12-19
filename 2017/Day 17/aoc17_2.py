file = open("aoc17_input.txt")
s = int(file.read())
file.close()

pos = 0
length = 1

for _ in range(50000000):
    pos = (pos + s) % length
    
    if pos == 0:
        print(length)
    
    length += 1
    pos = (pos + 1) % length

    if length % 10000000 == 9999999:
        print(f"Passed {length+1}")