file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

l = l[0].split(",")

boxes = [{} for _ in range(256)]
for w in l:
    label = w[:-1] if w[-1] == "-" else w[:-2]

    hash = 0
    for c in label:
        hash = (hash + ord(c)) * 17 % 256

    if w[-1] == "-":
        if label in boxes[hash]:
            boxes[hash].pop(label)
    else:
        strength = int(w.split("=")[1])
        boxes[hash][label] = strength

s = 0
for b in range(256):
    idx = 1
    for v in boxes[b].values():
        s += (b + 1) * idx * v
        idx += 1

print(s)