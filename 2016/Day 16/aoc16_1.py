file = open("aoc16_input.txt")
s = file.read()
file.close()

length = 272

def dragonize(s):
    return s + "0" + s[::-1].replace("0", "X").replace("1", "0").replace("X", "1")

while len(s) < length:
    s = dragonize(s)
s = s[:length]

checksum = s
while len(checksum) % 2 == 0:
    checksum = "".join("01"[checksum[j] == checksum[j+1]] for j in range(0, len(checksum), 2))

print(checksum)