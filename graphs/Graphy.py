import random
from graphs.WeghtedGraph import Graph
from abc import ABC
from queue import Queue

class Graphy:
    class Node(ABC):
        def __init__(self, label: str, value):
            self.label = label
            self.value = value

        def __str__(self):
            return f"{self.label} : {self.value}"

    def __init__(self):
        self.__nodes: dict[str, Graphy.Node] = {}
        self.__connections: dict[Graphy.Node, list[Graphy.Node]] = {}
        self.__count = 0

    def add_node(self, label: str, value):
        node = self.__nodes[label] = Graphy.Node(label, value)
        self.__connections[node] = []
        self.__count += 1

    def remove_node(self, label: str):
        node = self.__nodes[label]
        if node is None:
            raise ValueError("undefined node!")

        for lists in self.__connections.values():
            if lists.__contains__(node):
                lists.remove(node)

        self.__connections.pop(node)
        self.__nodes.pop(label)
        self.__count -= 1

    def connect(self, first: str, second: str):
        from_node = self.__nodes[first]
        to_node = self.__nodes[second]

        if from_node is None or to_node is None:
            raise ValueError("undefined node!")

        self.__connections[from_node].append(to_node)

    def disconnect(self, from_node: str, to_node: str):
        from_node = self.__nodes[from_node]
        to_node = self.__nodes[to_node]
        if from_node is None or to_node is None:
            raise ValueError("undefined node!")
        self.__connections[from_node].remove(to_node)

    def print_graph(self):
        for node in self.__nodes.values():
            if not self.__connections[node]:
                print(f"{node.label} has no connection!")
                continue
            neighbors = list(map(lambda n: n.label, self.__connections[node]))
            print(f"{node.label} connected by", neighbors)

    def has_cycle(self) -> bool:
        all = set()
        visiting = set()
        visited = set()

        for node in self.__nodes.values():
            all.add(node)

        while all:
            current = all.pop()
            result = self.__has_cycle(current, all, visiting, visited)
            if result:
                return True
        return False

    def __has_cycle(self, node: Node, all: set, visiting: set, visited: set) -> bool:
        visiting.add(node)
        for neighbor in self.__connections[node]:
            if visited.__contains__(neighbor):
                continue
            elif visiting.__contains__(neighbor):
                return True
            result = self.__has_cycle(neighbor, all, visiting, visited)
            if result:
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    def depth_first_iterate(self, root:str):
        node = Graphy.Node
        try:
            node = self.__nodes[root]
        except Exception as e:
            print("undefined node!")

        visited = set()
        stack = [node]

        for neighbor in self.__connections[node]:
            stack.append(neighbor)

        while stack:
            current = stack.pop()
            if visited.__contains__(current):
                continue
            print(current)
            visited.add(current)

            for neighbor in self.__connections[current]:
                if visited.__contains__(neighbor):
                    continue
                stack.append(neighbor)

    def breadth_first_iterate(self, root: str):
        node = Graphy.Node
        try:
            node = self.__nodes[root]
        except Exception as e:
            print("undefined node!")

        visited = set()
        queue = Queue()
        queue.put(node)
        for neighbor in self.__connections[node]:
            queue.put(neighbor)

        while not queue.empty():
            current = queue.get()
            if visited.__contains__(current):
                continue
            print(current)
            visited.add(current)

            for neighbor in self.__connections[current]:
                if visited.__contains__(neighbor):
                    continue
                queue.put(neighbor)








