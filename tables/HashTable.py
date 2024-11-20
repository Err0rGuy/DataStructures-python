class HashTable:
    class Node:
        def __init__(self, key: int, value):
            self.key = key
            self.value = value

        def __str__(self):
            return f"{self.key} : {self.value}"

    def __init__(self, capacity: int):
        self.count = 0
        self.source: list[list[HashTable.Node]] = [[]] * capacity

    def hash_function(self, key) -> int:
        return key % len(self.source)

    def insert(self, key: int, value):
        node = HashTable.Node(key, value)
        index = self.hash_function(key)
        self.source[index].append(node)
        self.count += 1

    def get(self, key: int):
        for element in self.source:
            for node in element:
                if node.key == key:
                    return node.value

    def contains(self, key: int):
        for element in self.source:
            for node in element:
                if node.key == key:
                    return True
        return False

    def remove(self, key: int):
        for element in self.source:
            for node in element:
                if node.key == key:
                    element.remove(node)
                    self.count += 1

    def show_table(self):
        for element in self.source:
            for node in element:
                print(node)


