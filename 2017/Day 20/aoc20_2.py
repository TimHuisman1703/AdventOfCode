file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

particles = []
left = 0

for i in range(len(l)):
	attr = [j[3:-1] for j in l[i].split(", ")]
	particles.append(tuple([int(j) for j in a.split(",")] for a in attr))

while len(particles):
	# Check for collisions
	slots = {}
	to_be_removed = []
	for part in particles:
		key = str(part[0])
		if key in slots.keys():
			to_be_removed.append(part)
			if slots[key] not in to_be_removed:
				to_be_removed.append(slots[key])
		else:
			slots.update({key: part})
	
	# print(f"Collided: {to_be_removed}")
	for part in to_be_removed:
		particles.remove(part)
	
	if len(particles) == 0:
		break
	
	# Remove extreme particles
	removed = True
	while removed:
		removed = False

		if len(particles) == 0:
			break

		extremes = [[[-1 for coord in range(3)] for degree in range(3)] for side in range(2)]
		for degree in range(3):
			for coord in range(3):
				minimum = (10**100, None)
				for i in range(len(particles)):
					part = particles[i]
					if part[degree][coord] < minimum[0]:
						minimum = (part[degree][coord], i)
				extremes[0][degree][coord] = minimum[1]
				
				maximum = (-10**100, None)
				for i in range(len(particles)):
					part = particles[i]
					if part[degree][coord] > maximum[0]:
						maximum = (part[degree][coord], i)
				extremes[1][degree][coord] = maximum[1]

		# print(extremes)
		
		to_be_removed = set()
		for side in range(2):
			for coord in range(3):
				x, y, z = extremes[side][0][coord], extremes[side][1][coord], extremes[side][2][coord]
				if x == y and y == z:
					# if len([*filter(lambda p: p[0][coord] == x and p[1][coord] == y and p[2][coord] == z, particles)]) == 1:
					to_be_removed.add(extremes[side][0][coord])
		
		removed = (len(to_be_removed) > 0)
		for i in sorted(to_be_removed)[::-1]:
			left += 1
			particles.pop(i)
	
	# Update velocity / position
	for p in particles:
		for degree in range(1, -1, -1):
			for coord in range(3):
				p[degree][coord] += p[degree+1][coord]
	
	print(len(particles))

print(left)