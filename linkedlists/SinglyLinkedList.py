class LinkedList:
    class Node:
        def __init__(self, value, default=None):
            self.value = value
            self.next: LinkedList.Node = default

        def __str__(self):
            return f"node: {self.value}"

    def __init__(self, default=None):
        self.first: LinkedList.Node = default
        self.last: LinkedList.Node = default
        self.count = 0

    def add_first(self, value):
        node = LinkedList.Node(value)
        if self.first is None:
            self.first = self.last = node
            self.count += 1
            return
        next = self.first
        self.first = node
        self.first.next = next
        self.count += 1

    def __previous(self, node: Node) -> Node:
        current = self.first
        while current.next is not None:
            if current.next == node:
                return current
            current = current.next

    def add_last(self, value):
        node = LinkedList.Node(value)
        if self.first is None:
            self.first = self.last = node
            self.count += 1
            return
        pre = self.last
        self.last = node
        pre.next = self.last
        self.count += 1

    def remove_first(self):
        if self.count == 0:
            raise Exception("is empty!")
        self.first = self.first.next
        self.count -= 1

    def remove_last(self):
        if self.count == 0:
            raise Exception("is empty!")
        self.last = self.__previous(self.last)
        self.last.next = None
        self.count -= 1

    def to_array(self) -> list:
        current = self.first
        result = []
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        a = self.first
        b = a.next
        self.last = self.first
        self.last.next = None
        while b is not None:
            c = b.next
            b.next = a
            a = b
            b = c
        self.first = a

    def get_kth_from_end(self, k: int):
        if k > self.count:
            raise ValueError("big number!")
        a = self.first
        b = self.first
        for i in range(0, k):
            b = b.next
        while b != self.last:
            a = a.next
            b = b.next

        return a

    def iterate(self):
        current = self.first
        while current is not None:
            print(current)
            current = current.next
