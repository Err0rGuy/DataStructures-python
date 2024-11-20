class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.count = 0

    def enqueue(self, item):
        self.stack1.append(item)
        self.count += 1


    def dequeue(self):
        if self.count == 0:
            raise Exception("is empty!")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.count == 0:
            raise Exception("is empty!")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

