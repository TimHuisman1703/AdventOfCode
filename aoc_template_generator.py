import os

YEAR = 2015
FILE = str(__file__)

location = "/".join(FILE.split("/")[:-1])

name = f"{location}/{YEAR}"
if not os.path.exists(name):
	os.mkdir(name)

for day in range(1, 26):
	name = f"{location}/{YEAR}/Day {day:02d}"
	if not os.path.exists(name):
		os.mkdir(name)

	for i in range(1, 2 + int(day != 25)):
		name = f"{location}/{YEAR}/Day {day:02d}/aoc{day:02d}_{i}.py"
		if not os.path.exists(name):
			f = open(name, "w")
			f.write(f'file = open("aoc{day:02d}_input.txt")\nl = file.read().split("\\n")\nfile.close()\n\n')
			f.close()
	
	name = f"{location}/{YEAR}/Day {day:02d}/aoc{day:02d}_input.txt"
	if not os.path.exists(name):
		f = open(name, "w")
		f.close()

print("Done!")