file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

particles = []

for i in range(len(l)):
	attr = [j[3:-1] for j in l[i].split(", ")]
	particles.append(tuple([i] + [[int(j) for j in a.split(",")] for a in attr]))

particles = sorted(particles, key=lambda x: sum(abs(j) for j in x[3]))

print(particles[0][0])