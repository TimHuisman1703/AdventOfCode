file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

output = {}
bot = {}
instructions = {}

def give_to_bot(bot_id, value):
    global bot

    if bot_id not in bot.keys():
        bot.update({bot_id: [value]})
    else:
        bot.update({bot_id: sorted(bot[bot_id] + [value])})

for instr in l:
    if instr[0] == "v":
        args = instr.split()
        value, bot_id = int(args[1]), int(args[5])
        give_to_bot(bot_id, value)
    else:
        instr = instr.replace("output ", "output -")
        args = instr.split()
        bot_id, low_to, high_to = int(args[1]), int(args[6]), int(args[11])
        instructions.update({bot_id: [low_to, high_to]})

while 1:
    has_two = []
    for bot_id, chips in bot.items():
        if len(chips) == 2:
            has_two.append(bot_id)
    
    if not has_two:
        break
    
    for bot_id in has_two:
        low_to, high_to = instructions[bot_id]
        low, high = bot[bot_id]

        give_to_bot(low_to, low)
        give_to_bot(high_to, high)

        bot.update({bot_id: []})

        print(f"{bot_id}: {low} / {high}")