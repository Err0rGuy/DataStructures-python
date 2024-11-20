class Tree:
    class Node:
        def __init__(self, value: int, default = None):
            self.value = value
            self.left_child: Tree.Node = default
            self.right_child:Tree.Node = default

        def __str__(self):
            return f"{self.value}"

    def __init__(self, default = None):
        self.count = 0
        self.root:Tree.Node = default

    def insert(self, value: int):
        node = Tree.Node(value)
        if self.root is None:
            self.root = node
            self.count += 1
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left_child is None:
                    current.left_child= node
                    break
                current = current.left_child
            else:
                if current.right_child is None:
                    current.right_child = node
                    break
                current = current.right_child

        self.count += 1

    def contains(self, value: int):
        if self.root is None:
            raise Exception("is empty!")
        current = self.root
        while not current is None:
            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child
            else:
                return True
        return False

    def remove(self, value: int):
        if self.root is None:
            raise Exception("is empty!")
        current = self.root
        while True:
            if value < current.value:
                if current.left_child.value == value:
                    current.left_child = None
                    break
                current = current.left_child
            elif value > current.value:
                if current.right_child.value == value:
                    current.right_child = None
                    break
            else:
                return
        self.count = 0
        self.__counter(self.root)

    def __counter(self, node: Node):
        if node is None:
            return
        self.count += 1
        self.__counter(node.left_child)
        self.__counter(node.right_child)

    def minimum(self):
        current = self.root
        b =  current
        while not current is None:
            b = current
            current = current.left_child
        return b.value

    def height(self):
        return self.__height(self.root)

    def __height(self, node) -> int:
        if node is None:
            return 0
        if node.left_child is None and node.right_child is None:
            return 0
        return 1 + max(self.__height(node.left_child), self.__height(node.right_child))

    def print_at_distance(self, distance: int):
        self.__print_at_distance(self.root, distance)

    def __print_at_distance(self, node: Node, distance: int):
        if node is None:
            return
        if distance == 0:
            print(node)

        self.__print_at_distance(node.left_child, distance - 1)
        self.__print_at_distance(node.right_child, distance - 1)


    def levelOrder(self):
        for i in range(self.height()):
            self.print_at_distance(i)

