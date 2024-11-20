class Array:
    def __init__(self, capacity):
        self.source = [None] * capacity
        self.count = 0

    def insert(self, item):
        if self.count == len(self.source):
            new_source = [None] * (len(self.source) * 2)
            for i in range(len(self.source)):
                new_source[i] = self.source[i]
            self.source = new_source

        self.source[self.count] = item
        self.count += 1

    def remove(self, index: int):
        if self.count == 0:
            raise Exception("is empty!")
        self.source[self.count - 1] = None
        self.count -= 1

    def contains(self, item) -> bool:
        for i in self.source:
            if i == item:
                return True
        return False

    def index_of(self, item) -> int:
        for i in range(len(self.source)):
            if self.source[i] == item:
                return i
        return  -1

    def item_of(self, index: int):
        return self.source[index]
