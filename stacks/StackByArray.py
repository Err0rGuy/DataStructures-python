class Stack:
    def __init__(self, capacity: int):
        self.source = [None] * capacity
        self.count = 0

    def push(self, item):
        self.source[self.count] = item
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception("is empty!")
        top = self.source[self.count - 1]
        self.source[self.count] = None
        self.count -= 1
        return top

    def peek(self):
        if self.count == 0:
            raise Exception("is empty!")
        return self.source[self.count]