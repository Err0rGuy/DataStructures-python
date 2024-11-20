class Stack:
    class Node:
        def __init__(self, value, default=None):
            self.value = value
            self.next: Stack.Node = default

    def __init__(self, default=None):
        self.head: Stack.Node = default
        self.tail: Stack.Node = default
        self.count = 0

    def previous(self, node: Node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next

    def push(self, item):
        if self.head is None:
            self.head = self.tail = self.Node(item)
            self.count += 1
            return

        pre_node = self.tail
        self.tail = self.Node(item)
        pre_node.next = self.tail
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception("is empty!")
        result = self.tail
        pre_node = self.previous(self.tail)
        self.tail = pre_node
        pre_node.next = None
        self.count -= 1
        return result
