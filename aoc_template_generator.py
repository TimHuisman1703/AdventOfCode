import os

YEAR = 2021
FILE = str(__file__)

location = "/".join(FILE.split("/")[:-1])

os.mkdir(f"{location}/{YEAR}")

for day in range(1, 26):
	os.mkdir(f"{location}/{YEAR}/Day {day:02d}")

	for i in range(1, 2 + int(day != 25)):
		f = open(f"{location}/{YEAR}/Day {day:02d}/aoc{day:02d}_{i}.py", "w")
		f.write(f'file = open("aoc{day:02d}_input.txt")\nl = file.read().split("\\n")\nfile.close()\n\n')
		f.close()
	
	f = open(f"{location}/{YEAR}/Day {day:02d}/aoc{day:02d}_input.txt", "w")
	f.close()

print("Done!")