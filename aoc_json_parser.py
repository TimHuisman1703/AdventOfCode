import json
import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
MAX_VALUE = 10**10

def unix_to_time(time):
    if time > 86400:
        return  "    >24h"
    
    hours = time // 3600
    minutes = (time // 60) % 60
    seconds = time % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"

class Member:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        if self.name == None:
            self.name = f"(anonymous user #{self.id})"
        
        self.stars = int(data["stars"])
        self.local_score = int(data["local_score"])
        self.global_score = int(data["global_score"])

        self.completion = [[MAX_VALUE, MAX_VALUE] for day in range(25)]

        for day, times in data["completion_day_level"].items():
            day = int(day) - 1
            for part, time in times.items():
                part, time = int(part) - 1, int(time["get_star_ts"])
                self.completion[day][part] = time
    
    def get_timestamp(self, year, day, part):
        start_event = 1448946000 + 31536000 * year + 86400 * ((year + 3) // 4)
        start = start_event + day * 86400
        end = self.completion[day][part]
        time = end - start

        return unix_to_time(time)

f = open(f"{DIRECTORY}/in.json", encoding="utf-8")
json_input = f.read()
leaderboard = json.loads(json_input)
f.close()

members = [Member(data) for data in leaderboard["members"].values()]

if len(members) == 0:
    print("There are no members in this leaderboard.")
    exit()

log_n = 1 + (len(members) > 9) + (len(members) > 99)
name_length = max(len(m.name) for m in members)

f = open(f"{DIRECTORY}/out.txt", "w", encoding="utf-8")

owner_id = leaderboard["owner_id"]
owner = f"(anonymous user #{owner_id})"
for member in members:
    if member.id == owner_id:
        owner = member.name
year = int(leaderboard["event"]) - 2015

# Print title
f.write(f"Leaderboard of {owner} (Advent of Code {year + 2015})\n\n")

# List by stars
members = sorted(members, key=lambda x: (-x.stars, -x.local_score, -x.global_score))
f.write("--- Stars ---")
for i in range(len(members)):
    member = members[i]
    f.write(f"\n{str(i + 1).rjust(log_n) + ')':<4} {str(member.name):<{name_length+1}} {member.stars:<4}" + "*" * member.stars)

# List by local score
members = sorted(members, key=lambda x: (-x.local_score, -x.global_score, -x.stars))
f.write("\n\n--- Local Score ---")
for i in range(len(members)):
    member = members[i]
    f.write(f"\n{str(i + 1).rjust(log_n) + ')':<4} {str(member.name):<{name_length+1}} {member.local_score}")

# List by global score
members = sorted(members, key=lambda x: (-x.global_score, -x.local_score, -x.stars))
f.write("\n\n--- Global Score ---")
for i in range(len(members)):
    member = members[i]
    f.write(f"\n{str(i + 1).rjust(log_n) + ')':<4} {str(member.name):<{name_length+1}} {member.global_score}")

# List by completion time per day and part
f.write("\n\n--- Completion Times ---")
first_day = True
for day in range(25):
    for part in range(2):
        members = sorted(members, key=lambda x: x.completion[day][part])
        if members[0].completion[day][part] < MAX_VALUE:
            if part == 0:
                f.write("\n" * (not first_day) + f"\nDay {day + 1}:")
                first_day = False
            f.write(f"\n  Part {part + 1}:")
        for i in range(len(members)):
            member = members[i]
            if member.completion[day][part] == MAX_VALUE:
                break
            f.write(f"\n    {str(i + 1).rjust(log_n) + ')':<4} {str(member.name):<{name_length+1}} {member.get_timestamp(year, day, part)}")
            if part == 1:
                f.write(f"    (+{unix_to_time(member.completion[day][1] - member.completion[day][0])})")
if first_day:
    f.write("\n  Nothing yet...")

f.close()
print("Done!")