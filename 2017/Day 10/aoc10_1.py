file = open("aoc10_input.txt")
lengths = [int(j) for j in file.read().split(",")]
file.close()

skip_size = 0
rotation = 0

nums = [*range(256)]

for l in lengths:
	nums = nums[l:] + nums[:l][::-1]
	rotation = (rotation + l) % len(nums)

	nums = nums[skip_size:] + nums[:skip_size]
	rotation = (rotation + skip_size) % len(nums)

	skip_size = (skip_size + 1) % len(nums)

nums = nums[-rotation:] + nums[:-rotation]

print(nums[0] * nums[1])