file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

def fight(user_hp, user_dam, user_arm, boss_hp, boss_dam, boss_arm):
	while 1:
		boss_hp -= max(1, user_dam - boss_arm)
		if boss_hp <= 0:
			return True
		
		user_hp -= max(1, boss_dam - user_arm)
		if user_hp <= 0:
			return False

import heapq

boss_hp = int(l[0].split()[2])
boss_dam = int(l[1].split()[1])
boss_arm = int(l[2].split()[1])

weapons = [
	(8, 4, 0),
	(10, 5, 0),
	(25, 6, 0),
	(40, 7, 0),
	(74, 8, 0)
]

armor = [
	(13, 0, 1),
	(31, 0, 2),
	(53, 0, 3),
	(75, 0, 4),
	(102, 0, 5),
]

rings = [
	(25, 1, 0),
	(50, 2, 0),
	(100, 3, 0),
	(20, 0, 1),
	(40, 0, 2),
	(80, 0, 3),
]

x_choices = weapons
y_choices = [(0, 0, 0)] + armor
z_choices = [(0, 0, 0)] + rings
for i in range(len(rings) - 1):
	for j in range(i + 1, len(rings)):
		z_choices.append((rings[i][0] + rings[j][0], rings[i][1] + rings[j][1], rings[i][2] + rings[j][2]))
z_choices = sorted(z_choices)

q = [(x_choices[0], 0, 0, 0)]
visited = set()
while 1:
	curr = heapq.heappop(q)
	visited.add(curr)

	
	if fight()

	if curr[0] < len(x_choices) - 1:
		cost = curr[0] + x_choices[curr[1] + 1] - x_choices[curr[1]]
		heapq.heappush(q, (cost, curr[1] + 1, curr[2], curr[3]))
	if curr[1] < len(y_choices) - 1:
		cost = curr[0] + y_choices[curr[2] + 1] - y_choices[curr[2]]
		heapq.heappush(q, (cost, curr[1], curr[2] + 1, curr[3]))
	if curr[2] < len(z_choices) - 1:
		cost = curr[0] + z_choices[curr[3] + 1] - z_choices[curr[3]]
		heapq.heappush(q, (cost, curr[1], curr[2], curr[3] + 1))