class Queue:
    def __init__(self, capacity: int):
        self.source = [None] * capacity
        self.rear = 0
        self.front = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == len(self.source):
            raise Exception("is fucking full bitch!")
        self.source[self.rear] = item
        self.rear = (self.rear + 1) % len(self.source)
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("is fucking empty bitch!")
        first = self.source[self.front]
        self.source[self.front] = None
        self.front = (self.front + 1) % len(self.source)
        self.count -= 1
        return first

    def peek(self):
        return self.source[self.front]

    def contains(self, item):
        return item in self.source

    def __str__(self):
        return f"{self.source}"

