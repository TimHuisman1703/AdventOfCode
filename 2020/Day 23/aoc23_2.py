file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

turns = 10000000
cups_amount = 1000000

cups_start = [int(j) for j in l[0]]

cups = [None]*cups_amount
cups[cups_amount-1] = Node(cups_amount, None)
for i in range(cups_amount-2, -1, -1):
    cups[i] = Node(i+1, cups[i+1])
for i in range(len(cups_start)-1):
    cups[cups_start[i]-1].set_next(cups[cups_start[i+1]-1])
cups[cups_start[-1]-1].set_next(cups[len(cups_start) % cups_amount])
cups[cups_amount-1].set_next(cups[cups_start[0]-1])

curr_cup = cups[cups_start[0]-1]

for i in range(turns):
    if(i % 1000000 == 0):
        print(i)
    
    first_removed_cup = curr_cup.get_next()
    curr_cup.set_next(first_removed_cup.get_next().get_next().get_next())

    value = value = (curr_cup.get_value() + cups_amount - 2) % cups_amount + 1
    while value == first_removed_cup.get_value() or value == first_removed_cup.get_next().get_value() or value == first_removed_cup.get_next().get_next().get_value():
        value = (value + cups_amount - 2) % cups_amount + 1
    
    insert_after_cup = cups[value-1]
    first_removed_cup.get_next().get_next().set_next(insert_after_cup.get_next())
    insert_after_cup.set_next(first_removed_cup)

    curr_cup = curr_cup.get_next()

print(cups[0].get_next().get_value()*cups[0].get_next().get_next().get_value())