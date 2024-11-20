class Node:
    def __init__(self, value: int, default=None):
        self.value = value
        self.left_child: Node = default
        self.right_child: Node = default
        self.height = 0

    def __Str__(self):
        return f"{self.value} : {self.height}"


class AVLTree:
    def __init__(self, default=None):
        self.__count = 0
        self.__root: Node = default

    def insert(self, value: int):
        self.__root = self.__insert(self.__root, value)
        self.__count += 1

    def contains(self, target):
        if self.__root is None:
            raise Exception("tree is empty")
        current: Node = self.__root
        while current:
            if target < current.value:
                current = current.left_child
            elif target > current.value:
                current = current.right_child
            else:
                return True
        return False

    def remove(self, target):
        if self.__root is None:
            raise Exception("tree is empty")

        current: Node = self.__root
        while current:
            if target < current.value:
                if current.left_child.value == target:
                    current.left_child = None
                    self.__set_height(current)
                    break
            elif target > current.value:
                if current.right_child.value == target:
                    current.right_child = None
                    self.__set_height(current)
                    break
            else:
                return
        self.__set_height(self.__root)
        self.__root = self.__balance(self.__root)
        self.__count = 0
        self.__counter(self.__root)

    def __counter(self, node: Node):
        if node is None:
            return
        self.__count += 1
        self.__counter(node.left_child)
        self.__counter(node.right_child)

    def __insert(self, node: Node, value: int) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left_child = self.__insert(node.left_child, value)
        else:
            node.right_child = self.__insert(node.right_child, value)

        self.__set_height(node)
        return self.__balance(node)

    def __height(self, node: Node) -> int:
        return -1 if (node is None) else node.height

    def __set_height(self, node: Node):
        node.height = max(self.__height(node.left_child), self.__height(node.right_child)) + 1

    def __balance_differance(self, node: Node) -> int:
        if node is None: return 0
        return self.__height(node.left_child) - self.__height(node.right_child)

    def __is_left_heavy(self, node: Node) -> bool:
        return self.__balance_differance(node) > 1

    def __is_right_heavy(self, node: Node) -> bool:
        return self.__balance_differance(node) < -1

    def __left_rotation(self, node: Node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        new_root.left_child = node
        self.__set_height(new_root)
        self.__set_height(node)
        return new_root

    def __right_rotation(self, node: Node):
        new_root = node.left_child
        node.left_child = new_root.right_child
        new_root.right_child = node
        self.__set_height(new_root)
        self.__set_height(node)
        return new_root

    def __balance(self, node: Node) -> Node:
        if self.__is_left_heavy(node):
            if self.__balance_differance(node.left_child) < 0:
                node.left_child = self.__left_rotation(node.left_child)
            return self.__right_rotation(node)
        elif self.__is_right_heavy(node):
            if self.__balance_differance(node.right_child) > 0:
                node.right_child = self.__right_rotation(node.right_child)
            return self.__left_rotation(node)
        return node
