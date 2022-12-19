file = open("aoc14_input.txt")
key = file.read()
file.close()

def knot_hash(s):
    lengths = [ord(j) for j in s] + [17, 31, 73, 47, 23]

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

    result = 0
    for i in range(0, 256, 16):
        result *= 1 << 8
        xor = 0
        for j in range(16):
            xor ^= nums[i+j]
        result += xor
    
    return result

c = 0
for i in range(128):
    hash = knot_hash(f"{key}-{i}")
    c += bin(hash).count("1")

print(c)