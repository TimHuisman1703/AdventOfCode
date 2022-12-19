file = open("aoc05_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

s = 0

for i in l:
    for j in range(len(i)-2):
        if i[j] == i[j+2]:
            br = False
            for k in range(2, len(i)//2):
                for m in range(len(i)+1-2*k):
                    if i.find(i[m:m+k], m+k) > -1:
                        print(i, i[j:j+3], i[m:m+k])
                        s += 1
                        br = True
                    if br:
                        break
                if br:
                    break
            break

print(s)