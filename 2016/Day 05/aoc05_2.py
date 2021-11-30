import hashlib

file = open("aoc05_input.txt")
door_id = file.read()
file.close()

code = ["-"]*8

i = 0
while "-" in code:
	result = hashlib.md5(f"{door_id}{i}".encode())
	hex_hash = result.hexdigest()

	if hex_hash[:5] == "00000":
		pos = int(hex_hash[5], 16)
		if pos < 8 and code[pos] == "-":
			code[pos] = hex_hash[6]
			
			print("".join(code))
	
	i += 1