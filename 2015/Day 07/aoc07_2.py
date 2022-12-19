file = open("aoc07_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

d = dict()

def get_wire_value(s):
    if s.isdigit():
        return int(s)
    
    e = d[s]
    es = e.split()
    r = 0

    if "NOT" in e:
        r = ~get_wire_value(es[1])
    elif "OR" in e:
        r = get_wire_value(es[0]) | get_wire_value(es[2])
    elif "AND" in e:
        r = get_wire_value(es[0]) & get_wire_value(es[2])
    elif "LSHIFT" in e:
        r = get_wire_value(es[0]) << get_wire_value(es[2])
    elif "RSHIFT" in e:
        r = get_wire_value(es[0]) >> get_wire_value(es[2])
    else:
        r = get_wire_value(es[0])


    r %= 65536
    d.update({s: str(r)})
    return r

for i in l:
    hs = i.split(" -> ")
    d.update({hs[1]: hs[0]})

d.update({"b": "3176"})

print(get_wire_value("a"))