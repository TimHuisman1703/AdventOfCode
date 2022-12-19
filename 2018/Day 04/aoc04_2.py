file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

l = sorted(l)

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
        
        if id not in timelapses.keys():
            timelapses.update({id: [0]*60})
        
        timelapse = timelapses[id]

        for i in range(asleep_at, awake_at):
            timelapse[i] += 1

max_minute = {}
for id, timelapse in timelapses.items():
    max_minute.update({id: max(timelapse)})

id, most_sleep = sorted(max_minute.items(), key=lambda x: -x[1])[0]
timelapse = timelapses[id]
minute = timelapse.index(most_sleep)

print(id, minute, id * minute)