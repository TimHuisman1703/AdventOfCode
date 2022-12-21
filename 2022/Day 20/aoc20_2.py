file = open("aoc20_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

l = [811589153 * j for j in l]

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self
        self.next = self
        self.marked = False
    
    def __repr__(self):
        return f"[{self.value}]"

zero_node = None

c = []
for i in range(len(l)):
    n = Node(l[i])
    if i > 0:
        n.prev = c[-1]
        c[-1].next = n
    if l[i] == 0:
        zero_node = n
    c.append(n)

c[0].prev = c[-1]
c[-1].next = c[0]

curr = c[0]
marked_count = 0
for i in range(10):
    for curr in c:
        value = curr.value % (len(l) - 1)
        if value:
            n = curr
            for _ in range(value):
                n = n.next
                if n == curr:
                    n = n.next
            
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            
            curr.prev = n
            curr.next = n.next
            n.next.prev = curr
            n.next = curr
        
    print(f"i = {i + 1} / 10")

s = 0
curr = zero_node
for _ in range(3):
    for _ in range(1000):
        curr = curr.next
    s += curr.value

print(s)