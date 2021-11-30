file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

l = sorted(l)

total_sleep = {}
timelapses = {}

id = 0
asleep_at = 0

for s in l:
	args = s.split()

	if "Guard" in args:
		id = int(args[3][1:])
	elif "falls" in args:
		asleep_at = int(args[1][3:5])
	elif "wakes":
		awake_at = int(args[1][3:5])
		nap_length = awake_at - asleep_at
		
		if id not in total_sleep.keys():
			total_sleep.update({id: 0})
			timelapses.update({id: [0]*60})
		
		total_sleep.update({id: total_sleep[id] + nap_length})
		timelapse = timelapses[id]

		for i in range(asleep_at, awake_at):
			timelapse[i] += 1

id = sorted(total_sleep.items(), key=lambda x: -x[1])[0][0]
timelapse = timelapses[id]
most_sleep = max(timelapse)
minute = timelapse.index(most_sleep)

print(id, minute, id * minute)