file = open("aoc10_input.txt")
lengths = [ord(j) for j in file.read()] + [17, 31, 73, 47, 23]
file.close()

skip_size = 0
rotation = 0

nums = [*range(256)]

for _ in range(64):
    for l in lengths:
        nums = nums[l:] + nums[:l][::-1]
        rotation = (rotation + l) % len(nums)

        nums = nums[skip_size:] + nums[:skip_size]
        rotation = (rotation + skip_size) % len(nums)

        skip_size = (skip_size + 1) % len(nums)

nums = nums[-rotation:] + nums[:-rotation]

result = ""
for i in range(0, 256, 16):
    xor = 0
    for j in range(16):
        xor ^= nums[i+j]
    result += hex(xor)[2:].zfill(2)

print(result)