class Queue:
    class Node:
        def __init__(self, value, default=None):
            self.value = value
            self.next: Queue.Node = default

        def __str__(self):
            return f'{self.value}'

    def __init__(self, default=None):
        self.first: Queue.Node = default
        self.last: Queue.Node = default
        self.count = 0

    def previous(self, node: Node) -> Node:
        current = self.first
        while not current is None:
            if current.next == node:
                return current
            current = current.next

    def enqueue(self, value):
        if self.first is None:
            self.first = self.last = self.Node(value)
            self.count += 1
            return
        pre_node = self.last
        self.last = self.Node(value)
        pre_node.next = self.last
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("is empty!")
        front = self.first
        self.first = self.first.next
        self.count -= 1
        return front
