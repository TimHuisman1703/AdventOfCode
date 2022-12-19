file = open("aoc14_input.txt")
steps = int(file.read())
file.close()

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value

        if prev and next:
            self.prev = prev
            self.next = next
        else:
            self.prev = self
            self.next = self
    
    def set_next(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

size = 2
head = a = Node(3)
b = Node(7)
a.set_next(b)

while size < steps + 10:
    i, j = a.value, b.value
    r = i + j

    if r < 10:
        head.prev.set_next(Node(r))
        size += 1
    else:
        head.prev.set_next(Node(1))
        head.prev.set_next(Node(r % 10))
        size += 2
    
    while i + 1:
        a = a.next
        i -= 1
    while j + 1:
        b = b.next
        j -= 1

curr = head
for _ in range(steps):
    curr = curr.next

r = 0
for _ in range(10):
    r = 10 * r + curr.value
    curr = curr.next

print(r)