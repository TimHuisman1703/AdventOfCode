file = open("aoc09_input.txt")
args = file.read().split()
file.close()

players = int(args[0])
last = int(args[6]) * 100

class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = self
        self.next = self

class CLL:
    def __init__(self):
        self.origin = None
        self.head = None
        self.count = 0
    
    def add(self, data):
        node = Node(data)

        if self.head == None:
            self.origin = node
            self.head = node
            self.count = 1
            return
        
        self.head.prev.next = node
        node.prev = self.head.prev
        self.head.prev = node
        node.next = self.head
        self.count += 1
        return
    
    def get(self):
        return self.head.data
    
    def remove(self):
        if self.count == 1:
            self.head = None
            self.origin = None
            self.count = 0
            return
        
        if self.head == self.origin:
            self.origin = self.head.next
        
        self.head.next.prev = self.head.prev
        self.head.prev.next = self.head.next

        node = self.head
        self.head = self.head.next
        self.count -= 1

        return node.data
    
    def rotate(self, amount):
        if amount > 0:
            for _ in range(amount):
                self.head = self.head.next
        else:
            for _ in range(-amount):
                self.head = self.head.prev
    
    def size(self):
        return self.count
    
    def display(self):
        print("[", end="")

        if self.count:
            current = self.origin

            if current == self.head:
                print(f">{current.data}<", end="")
            else:
                print(current.data, end="")

            while current.next != self.origin:
                current = current.next
                
                if current == self.head:
                    print(f", >{current.data}<", end="")
                else:
                    print(f", {current.data}", end="")
        
        print("]")

l = CLL()
l.add(0)
pos = 0
points = [0 for _ in range(players)]

i = 1
while i <= last:
    if i % 23:
        l.rotate(1)
        l.add(i)
    else:
        l.rotate(-8)
        points[(i-1) % players] += i + l.get()
        l.remove()
        l.rotate(1)

    if i % 10000 == 9999:
        print(f"{i+1}/{last+1}")

    i += 1

print(max(points))