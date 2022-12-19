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

squares = set()
for iy in range(128):
    hash = knot_hash(f"{key}-{iy}")
    b = bin(hash)[2:].zfill(128)
    for ix in range(128):
        if b[ix] == "1":
            squares.add((ix, iy))

regions = 0
while len(squares):
    regions += 1
    initial_square, *_ = [*squares]
    queue = [initial_square]

    while queue:
        current = queue.pop(0)
        squares.remove(current)
        x, y = current

        for ix, iy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if ix < 0 or ix > 127 or iy < 0 or iy > 127:
                continue

            if (ix, iy) in squares and (ix, iy) not in queue:
                queue.append((ix, iy))

print(regions)