def has_abba(s):
    for i in range(len(s)-3):
        if s[i] != s[i+1] and s[i:i+2] == s[i+2:i+4][::-1]:
            return True

    return False

file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

c = 0

for ip in l:
    out_has_abba = False
    in_has_abba = False

    while "]" in ip:
        index = ip.index("]")
        segment, ip = ip[:index], ip[index+1:]

        out_segment, in_segment = segment.split("[")

        out_has_abba |= has_abba(out_segment)
        in_has_abba |= has_abba(in_segment)
    
    out_has_abba |= has_abba(ip)

    if out_has_abba and not in_has_abba:
        c += 1

print(c)