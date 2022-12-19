file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

def play_game(old_cards):
    cards = [[], []]
    for i in range(2):
        cards[i] = [j for j in old_cards[i]]
    print(cards)

    rounds = dict()
    
    while len(cards[0]) and len(cards[1]):
        try:
            if rounds[str(cards)]:
                return 0, cards
        except:
            rounds.setdefault(str(cards), True)

        top = [-1, -1]
        for i in range(2):
            top[i] = cards[i][0]
            cards[i] = cards[i][1:]
        
        winner = -1
        if len(cards[0]) >= top[0] and len(cards[1]) >= top[1]:
            winner, garbage = play_game([cards[0][:top[0]], cards[1][:top[1]]])
        else:
            winner = int(top[0] < top[1])
                
        if winner == 0:
            cards[0].append(top[0])
            cards[0].append(top[1])
        else:
            cards[1].append(top[1])
            cards[1].append(top[0])
    
    return int(len(cards[1]) > 0), cards

i = 1

cards = [[], []]
while l[i] != "":
    cards[0].append(int(l[i]))
    i += 1

i += 2
while i < len(l):
    cards[1].append(int(l[i]))
    i += 1

winner, cards = play_game(cards)

print(cards)

p = 0
for i in range(len(cards[winner])):
    p += (len(cards[winner])-i)*cards[winner][i]

print(p)