file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

class Group:
	def __init__(self, desc):
		args = desc.split()

		self.units = int(args[0])
		self.hp = int(args[4])

		self.immune = []
		self.weak = []
		if "(" in desc:
			info = desc.replace(",", "").split("(")[1].split(")")[0].split("; ")

			for i in info:
				words = i.split()
				if words[0] == "immune":
					self.immune = words[2:]
				else:
					self.weak = words[2:]

		self.attack_power = int(args[-6])
		self.attack_type = args[-5]
		self.initiative = int(args[-1])
	
	def effective_power(self):
		return self.units * self.attack_power
	
	def damage_taken(self, effective_power, attack_type):
		return effective_power * (1 + (attack_type in self.weak) - (attack_type in self.immune))
	
	def damage(self, effective_power, attack_type):
		damage = self.damage_taken(effective_power, attack_type)
		units_lost = damage // self.hp
		self.units -= units_lost
		return units_lost > 0

def survivors(boost):
	groups = []

	i = 1
	immune_system = True
	while i < len(l):
		if l[i] == "":
			immune_system = False
			i += 2
		
		g = Group(l[i])
		g.side = immune_system
		groups.append(g)

		i += 1
	
	for g in groups:
		if g.side:
			g.attack_power += boost
	
	while any(j.side for j in groups) and any(not j.side for j in groups):
		groups = sorted(groups, key=lambda x: (-x.effective_power(), -x.initiative))
		attacking = {}

		for g in groups:
			opponents = [j for j in groups if j.side != g.side]
			opponents = sorted(opponents, key=lambda x: (x in attacking.values(), -x.damage_taken(g.effective_power(), g.attack_type)))

			if opponents[0] not in attacking.values() and opponents[0].damage_taken(g.effective_power(), g.attack_type) > 0:
				attacking[g] = opponents[0]
		
		damaged = False
		groups = sorted(groups, key=lambda x: -x.initiative)
		for g in groups:
			if g.units <= 0 or g not in attacking.keys():
				continue
			
			opponent = attacking[g]
			damaged |= opponent.damage(g.effective_power(), g.attack_type)
		
		if not damaged:
			return {}
		
		groups = [j for j in groups if j.units > 0]

	return groups

max_boost = 1
while any(not j.side for j in survivors(max_boost)):
	max_boost *= 2
min_boost = max_boost // 2

while min_boost != max_boost:
	mid = (min_boost + max_boost) // 2

	groups = survivors(mid)
	if any(j.side for j in survivors(mid)):
		max_boost = mid
	else:
		min_boost = mid + 1

groups = survivors(max_boost)

s = 0
for g in groups:
	s += g.units
print(s)