file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

d = {}

for i in l:
    x = y = 0
    j = 0
    while j < len(i):
        if i[j] == "w":
            x -= 1
        elif i[j] == "e":
            x += 1
        elif i[j] == "n":
            y -= 1
            j += 1
            if i[j] == "w":
                x -= 1
        else:
            y += 1
            j += 1
            if i[j] == "e":
                x += 1
        j += 1
    
    try:
        d.update({str(x)+","+str(y): 1-d[str(x)+","+str(y)]})
    except:
        d.setdefault(str(x)+","+str(y), 1)

print(sum(d.values()))