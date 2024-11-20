class Radix:
    class Node:
        def __init__(self, value):
            self.value = value
            self.is_end_of_word: bool = False
            self.children: dict[str, Radix.Node] = {}
        def add_child(self, char: str):
            self.children[char] = Radix.Node(char)
        def remove_child(self, char: str):
            self.children.pop(char)
        def get_child(self, char: str):
            return self.children[char]
        def get_all_children(self):
            return list(self.children.values())
        def has_this_child(self, char: str) -> bool:
            return self.children.__contains__(char)
        def has_children(self) -> bool:
            return True if self.children else False
        def __str__(self):
            return f"{self.value} -> {self.is_end_of_word}"

    __root = Node('')

    def __init__(self):
        self.__count_of_chars = 0
        self.__count_of_words = 0

    def is_empty(self) -> bool:
        return self.__count_of_chars == 0
    def insert(self, word: str):
        current = self.__root
        for ch in word:
            if not current.has_this_child(ch):
                current.add_child(ch)
                self.__count_of_chars += 1
            current = current.get_child(ch)
        self.__count_of_words += 1
        current.is_end_of_word = True


    def contains(self, word: str) -> bool:
        if self.is_empty():
            raise ValueError("is Empty!")
        current = self.__root
        for ch in word:
            if not current.has_this_child(ch):
                return False
            current = current.get_child(ch)

        return current.is_end_of_word

    def remove(self, word: str):
        self.__remove(self.__root, word, 0)

    def __remove(self, node: Node, word: str, index: int):
        if index == len(word):
            node.is_end_of_word = False
            return
        ch = word[index]
        child = node.get_child(ch)
        if child is None:
            return
        self.__remove(child, word, index + 1)
        if not child.is_end_of_word and not child.has_children():
            node.remove_child(ch)

    def traversal_depth_first(self):
        self.__traversal_depth_first(self.__root)

    def __traversal_depth_first(self, node:Node):
        if node is None:
            return
        if not node == self.__root:
            print(node)

        for other in node.get_all_children():
            self.__traversal_depth_first(other)























