file = open("aoc01_input.txt")
l = file.read().split("\n")
file.close()

d = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

s = 0
for w in l:
    first = last = -1
    for i in range(len(w)):
        for key, value in d.items():
            if w[i:i + len(key)] == key:
                if first == -1:
                    first = value
                last = value
    s += first * 10 + last

print(s)