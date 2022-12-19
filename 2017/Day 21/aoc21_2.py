file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

ITERATIONS = 18

def rotate(s):
    rows = s.split("/")
    size = len(rows)
    cols = ["".join(rows[size-1-jy][jx] for jy in range(size)) for jx in range(size)]
    return "/".join(cols)

def flip(s):
    rows = s.split("/")
    return "/".join(j[::-1] for j in rows)

d = {}
for instr in l:
    args = instr.split(" => ")
    d.update({args[0]: args[1]})

g = ".#./..#/###".split("/")

for iter in range(ITERATIONS):
    ng = []
    size = len(g)
    sub_size = 2 + size % 2

    for iy in range(0, size, sub_size):
        rows = ["" for _ in range(sub_size + 1)]

        for ix in range(0, size, sub_size):
            key = "/".join(g[iy + j][ix:ix + sub_size] for j in range(sub_size))
            
            for i in range(8):
                if key in d.keys():
                    break

                key = rotate(key)
                if i == 3:
                    key = flip(key)
            
            square = d[key].split("/")

            for i in range(sub_size + 1):
                rows[i] += square[i]
        
        ng.extend(rows)
    
    g = ng

    print(f"Iterations done: {iter + 1}")

print(sum(j.count("#") for j in g))