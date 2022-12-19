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
        print(a)
        for j in range(len(w)):
            if w[j] in a:
                x = a[a.index(w[j])+4:].split()[0]

                if w[j] == "byr":
                    if len(x) != 4 or int(x) < 1920 or int(x) > 2002:
                        c = False
                        print("Birth Year Out Of Range")
                elif w[j] == "iyr":
                    if len(x) != 4 or int(x) < 2010 or int(x) > 2020:
                        c = False
                        print("Issue Year Out Of Range")
                elif w[j] == "eyr":
                    if len(x) != 4 or int(x) < 2020 or int(x) > 2030:
                        c = False
                        print("Expiration Year Out Of Range")
                elif w[j] == "hgt":
                    if len(x) < 3:
                        c = False
                    elif x[-2:] == "cm":
                        if int(x[:-2]) < 150 or int(x[:-2]) > 193:
                            c = False
                            print("Height Out Of Range (Cm)")
                    elif x[-2:] == "in":
                        if(int(x[:-2]) < 59 or int(x[:-2]) > 76):
                            c = False
                            print("Height Out Of Range (In)")
                    else:
                        c = False
                        print("Invalid Unit")
                elif w[j] == "hcl":
                    if x[0] == "#" and len(x) == 7:
                        for k in x[1:]:
                            if not k in "0123456789abcdef":
                                c = False
                                print("Hair Color contains Non-Hex Digits")
                    else:
                        c = False
                        print("Hair Color not in #XXXXXX Form")
                elif w[j] == "ecl":
                    if x not in "amb|blu|brn|gry|grn|hzl|oth":
                        print("Invalid Eye Color")
                        c = False
                elif w[j] == "pid":
                    if len(x) != 9 or int(x) < 0:
                        print("Invalid PID")
                        c = False
            else:
                print("Doesn't Contain "+w[j].upper())
                c = False
        if c:
            s += 1
        a = ""
        t += 1
    else:
        a += " " + l[i]
print(t, s)