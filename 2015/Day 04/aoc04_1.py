file = open("aoc04_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

import hashlib

code = bytes(l[0], "utf-8")

n = 0
result = hashlib.md5(code + bytes(str(n).zfill(6), "utf-8")).digest()
while result[0] or result[1] or result[2]//16:
    if n%100000 == 0:
        print(n)
    n += 1
    result = hashlib.md5(code + bytes(str(n).zfill(6), "utf-8")).digest()

print(n)
print(result)