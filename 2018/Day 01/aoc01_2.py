file = open("aoc01_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

current = 0
visited = set()
while 1:
    for i in l:
        if current in visited:
            print(current)
            exit()

        visited.add(current)
        current += i