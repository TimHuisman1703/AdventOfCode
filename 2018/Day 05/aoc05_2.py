file = open("aoc05_input.txt")
s = file.read()
file.close()

types = set(s.lower())

lengths = {}

for t in types:
    print(t)
    
    fs = s.replace(t, "").replace(t.upper(), "")

    i = 0
    while i < len(fs)-1:
        c = sorted(fs[i:i+2])
        
        if c[0].isupper() and c[1].islower() and c[0].lower() == c[1]:
            fs = fs[:i] + fs[i+2:]
            i -= int(i > 0)
        else:
            i += 1

    lengths.update({t: len(fs)})

best = sorted(lengths.items(), key=lambda x: x[1])[0]
print(best[1])