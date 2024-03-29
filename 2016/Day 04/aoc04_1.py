file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

s = 0

for room in l:
    room = room.split("-")
    name = "".join(room[:-1])
    sector_id = int(room[-1].split("[")[0])
    checksum = room[-1].split("[")[1][:-1]

    ranking = []

    for c in [chr(i) for i in range(97, 123)]:
        ranking.append((c, name.count(c)))
    
    ranking = sorted(ranking, key = lambda x: -x[1])

    for i in range(len(checksum)):
        if checksum[i] != ranking[i][0]:
            break
    else:
        s += sector_id

print(s)