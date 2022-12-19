file = open("aoc16_input.txt")
s = file.read()
file.close()

length = 35651584

def dragonize(s):
    return s + "0" + s[::-1].replace("0", "X").replace("1", "0").replace("X", "1")

while len(s) < length:
    s = dragonize(s)
s = s[:length]

print("Done dragonizing")

power = bin(length)[::-1].index("1")
segment_length = 2**power

checksum = "".join("01"[(s[j:j+segment_length].count("1") + 1) % 2] for j in range(0, length, segment_length))
print(checksum)