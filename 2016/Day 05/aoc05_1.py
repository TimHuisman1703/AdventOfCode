import hashlib

file = open("aoc05_input.txt")
door_id = file.read()
file.close()

code = ""

c = 0
i = 0
while c < 8:
	result = hashlib.md5(f"{door_id}{i}".encode())
	hex_hash = result.hexdigest()

	if hex_hash[:5] == "00000":
		code += hex_hash[5]
		c += 1
	
	i += 1

print(code)