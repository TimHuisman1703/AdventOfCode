import re
import hashlib

file = open("aoc14_input.txt")
salt = file.read()
file.close()

has_three = []
has_five = []

i = 0
indexes = set()
ultimatum = -1
while i < ultimatum or ultimatum == -1:
	hex_hash = f"{salt}{i}"

	for _ in range(2017):
		hex_hash = hashlib.md5(hex_hash.encode()).hexdigest()

	char_three_times = re.findall("(.)\\1{2,}", hex_hash)
	char_five_times = set(re.findall("(.)\\1{4,}", hex_hash))
	
	if char_three_times:
		has_three.append((i, char_three_times[0]))
	if char_five_times:
		for letter in char_five_times:
			valid_tuples = [*filter(lambda x: x[0] >= i - 1000 and x[0] < i and letter == x[1], has_three)]

			prev_indexes = set(map(lambda x: x[0], valid_tuples))
			indexes = indexes.union(prev_indexes)

			for index, h in valid_tuples:
				print(f'{index} ({hashlib.md5(f"{salt}{index}".encode()).hexdigest()}) matches to {i} ({hashlib.md5(f"{salt}{i}".encode()).hexdigest()}) ({len(indexes)})')
	i += 1
	
	if len(indexes) >= 64 and ultimatum == -1:
		ultimatum = i + 1000

print(sorted(indexes)[63])