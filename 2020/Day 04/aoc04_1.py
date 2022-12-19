file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

w = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

s = 0
t = 0
a = ""
for i in range(len(l)+1):
    if i == len(l) or l[i] == "":
        c = True
        for j in range(len(w)):
            if(w[j] not in a):
                print(w[j])
                c = False
        if c:
            s += 1
        else:
            print(a)
        a = ""
        t += 1
    else:
        a += " " + l[i]
print(t, s)