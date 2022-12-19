file = open("aoc11_input.txt")
sn = int(file.read())
file.close()

def calc_power(x, y, sn):
    rack_id = x + 10
    return (rack_id * y + sn) * rack_id // 100 % 10 - 5

power = [[calc_power(ix, iy, sn) for ix in range(300)] for iy in range(300)]

best = ((-1, -1), 0)

for iy in range(298):
    for ix in range(298):
        total_power = sum(sum(row[ix:ix+3]) for row in power[iy:iy+3])

        if total_power > best[1]:
            best = ((ix, iy), total_power)

print(f"{best[0][0]},{best[0][1]}")