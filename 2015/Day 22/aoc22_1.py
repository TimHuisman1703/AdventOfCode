file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

import heapq

boss_hp = int(l[0].split()[2])
boss_dam = int(l[1].split()[1])

player_hp = 50
mana = 500

# cost, player_hp, boss_hp, mana, shield_time, poison_time, recharge_time, player_turn
q = [(0, player_hp, boss_hp, mana, 0, 0, 0, True)]

while 1:
    cost, player_hp, boss_hp, mana, shield_time, poison_time, recharge_time, player_turn = heapq.heappop(q)

    boss_hp -= 3 * (poison_time > 0)

    if player_hp <= 0:
        continue
    if boss_hp <= 0:
        print(cost)
        break

    mana += 101 * (recharge_time > 0)
    
    if player_turn:
        # Magic Missile
        if mana >= 53:
            heapq.heappush(q, (cost + 53, player_hp, boss_hp - 4, mana  - 53, shield_time - 1, poison_time - 1, recharge_time - 1, False))
        
        # Drain
        if mana >= 73:
            heapq.heappush(q, (cost + 73, player_hp + 2, boss_hp - 2, mana - 73, shield_time - 1, poison_time - 1, recharge_time - 1, False))
        
        # Shield
        if mana >= 113 and shield_time <= 1:
            heapq.heappush(q, (cost + 113, player_hp, boss_hp, mana - 113, 6, poison_time - 1, recharge_time - 1, False))
        
        # Poison
        if mana >= 173 and poison_time <= 1:
            heapq.heappush(q, (cost + 173, player_hp, boss_hp, mana - 173, shield_time - 1, 6, recharge_time - 1, False))

        # Recharge
        if mana >= 229 and recharge_time < 1:
            heapq.heappush(q, (cost + 229, player_hp, boss_hp, mana - 229, shield_time - 1, poison_time - 1, 5, False))
    else:
        heapq.heappush(q, (cost, player_hp - max(1, boss_dam - 7 * (shield_time > 0)), boss_hp, mana, shield_time - 1, poison_time - 1, recharge_time - 1, True))