import math


class Heap:
    def __init__(self):
        self.heap = []
        self.count = 0

    def insert(self, item: int):
        self.heap.insert(self.count, item)
        self.count += 1
        self.bubble_up()

    def remove(self):
        if self.count == 0:
            raise Exception("heap is empty")
        root = self.heap[0]
        self.heap[0] = self.heap[self.count - 1]
        self.count -= 1
        self.heap[self.count] = 0
        self.bubble_down()
        return root

    def parent_index(self, index: int):
        return (index - 1) // 2

    def left_child_index(self, index: int):
        return (index * 2) + 1

    def right_child_index(self, index: int):
        return (index * 2) + 2

    def big_child_index(self, index: int):
        left = self.left_child_index(index)
        right = self.right_child_index(index)

        if left > self.count:
            return index
        if right > self.count:
            return left
        return left if (self.heap[left] > self.heap[right]) else right

    def bubble_up(self):
        index = self.count - 1
        while index > 0 and self.heap[index] > self.heap[self.parent_index(index)]:
            parent = self.parent_index(index)
            self.swap(index, parent)
            index = parent

    def bubble_down(self):
        index = 0
        while index <= self.count and self.heap[index] < self.heap[self.big_child_index(index)]:
            child = self.big_child_index(index)
            self.swap(index, child)
            index = child

    def swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
