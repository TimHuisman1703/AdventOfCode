file = open("aoc11_input.txt")
sn = int(file.read())
file.close()

def calc_power(x, y, sn):
    rack_id = x + 10
    return (rack_id * y + sn) * rack_id // 100 % 10 - 5

power = [[calc_power(ix, iy, sn) for ix in range(300)] for iy in range(300)]

best = ((-1, -1, -1), 0)

for iy in range(298):
    print(f"{iy+1}/{298}")
    for ix in range(298):
        total_power = 0
        for size in range(1, 301 - max(ix, iy)):
            total_power += sum(power[iy+size-1][ix:ix+size]) + sum(power[iy+j][ix+size-1] for j in range(size-1))

            if total_power > best[1]:
                best = ((ix, iy, size), total_power)

print(f"{best[0][0]},{best[0][1]},{best[0][2]}")