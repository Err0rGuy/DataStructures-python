class PriorityQueue:
    def __init__(self, capacity: int):
        self.source = [0] * capacity
        self.count = 0

    def __resize(self):
        new_source = [0] * len(self.source) * 2
        for i in range(len(self.source)):
            new_source.insert(i, self.source[i])
        self.source = new_source

    def __str__(self):
        return f"{self.source}"

    def insert(self, item):
        if self.count == len(self.source):
            self.__resize()
        i = 0
        for i in range(self.count - 1, -1):
            if item < self.source[i]:
                self.source[i + 1] = self.source[i]
            else:
                break
        self.source[i + 1] = item
        self.count += 1
