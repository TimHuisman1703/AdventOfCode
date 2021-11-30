import hashlib

file = open("aoc17_input.txt")
password = file.read()
file.close()

width = height = 4

queue = [(0, 0, "")]
max_length = 0

while queue:
	x, y, path = queue.pop(0)
	hex_hash = hashlib.md5(f"{password}{path}".encode()).hexdigest()
	
	if x == 3 and y == 3:
		max_length = len(path)
		continue

	if y > 0 and hex_hash[0] in "bcdef":
		queue.append((x, y - 1, path + "U"))
	if y < height-1 and hex_hash[1] in "bcdef":
		queue.append((x, y + 1, path + "D"))
	if x > 0 and hex_hash[2] in "bcdef":
		queue.append((x - 1, y, path + "L"))
	if x < width-1 and hex_hash[3] in "bcdef":
		queue.append((x + 1, y, path + "R"))

print(max_length)