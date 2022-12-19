file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

nums = [int(j) for j in l[0].split(",")]

cards = []

for i in range(2, len(l), 6):
    card = []
    for j in range(i, i+5):
        card.append([int(j) for j in l[j].split()])

    cards.append(card)

def has_bingo(card, s):
    for i in range(5):
        win = True
        for j in range(5):
            if card[j][i] not in s:
                win = False
        if win:
            return True
    
    for i in range(5):
        win = True
        for j in range(5):
            if card[i][j] not in s:
                win = False
        if win:
            return True
    
    return False

drawn = set()
for i in range(len(nums)):
    num = nums[i]
    drawn.add(num)

    to_remove = []
    
    for c in cards:
        if has_bingo(c, drawn):
            if len(cards) == 1:
                su = 0
                for row in c:
                    for i in row:
                        if i not in drawn:
                            su += i
                
                print(num * su)
            
            to_remove.append(c)
    
    for i in to_remove:
        cards.remove(i)