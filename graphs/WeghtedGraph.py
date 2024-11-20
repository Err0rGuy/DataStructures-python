import heapq
import random
import sys
from queue import PriorityQueue


class Node:
    def __init__(self, label: str, value):
        self.label = label
        self.value = value
        self.edges: list[Edge] = []

    def connect(self, node, weight: int):
        self.edges.append(Edge(self, node, weight))

    def disconnect(self, node):
        for edge in self.edges:
            if edge.to_node == node:
                self.edges.remove(edge)

    def __Str__(self):
        return f"{self.label} : {self.value}"


class Edge:
    def __init__(self, node1: Node, node2: Node, weight: int):
        self.from_node = node1
        self.to_node = node2
        self.weight = weight

    def __str__(self):
        return f"{self.from_node.label} : {self.to_node.label} : {self.weight}"


class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.count = 0

    def add_node(self, label: str, value):
        node = Node(label, value)
        self.nodes[label] = node
        self.count += 1

    def remove_node(self, label: str):
        node = self.nodes[label]

        for other in self.nodes.values():
            for edge in other.edges:
                if edge.to_node == node:
                    other.edges.remove(edge)
        self.nodes.pop(label)
        self.count -= 1

    def connection(self, node1: str, node2: str, weight: int):
        from_node = self.nodes[node1]
        to_node = self.nodes[node2]

        if from_node is None or to_node is None:
            return

        from_node.connect(to_node, weight)
        to_node.connect(from_node, weight)

    def disconnection(self, node1: str, node2: str):
        from_node = self.nodes[node1]
        to_node = self.nodes[node2]

        if from_node is None or to_node is None:
            return

        from_node.disconnect(to_node)
        to_node.disconnect(from_node)

    def printing(self):
        visited = set()
        for i in self.nodes.values():
            visited.add(i)
            for j in i.edges:
                if j.to_node not in visited:
                    print(f"{i.label} <-->  {j.to_node.label} : {j.weight}")

    def neighbors(self, label):
        node = self.nodes[label]
        if node is None:
            return
        for i in node.edges:
            print(i.to_node.label)

    def find_shortest_way(self, node1: str, node2: str):
        from_node = self.nodes[node1]
        to_node = self.nodes[node2]

        visited = set()
        pre_node: dict[Node, Node] = {}
        distances: dict[Node, int] = {}
        queue: list[list] = []
        for i in self.nodes.values():
            distances[i] = sys.maxsize
        distances[from_node] = 0
        heapq.heappush(queue, [distances[to_node], to_node])
        heapq.heappush(queue, [distances[from_node], from_node])

        while queue:
            current: Node = heapq.heappop(queue)[1]
            if visited.__contains__(current):
                continue
            visited.add(current)
            for edge in current.edges:
                if edge.to_node not in visited:
                    new_dist = distances[current] + edge.weight
                    if new_dist < distances[edge.to_node]:
                        distances[edge.to_node] = new_dist
                        pre_node[edge.to_node] = current
                        heapq.heappush(queue, [distances[edge.to_node], edge.to_node])

        path = [to_node.label]
        previous = pre_node[to_node]
        while not previous is None:
            path.append(previous.label)
            previous = pre_node.get(previous)

        return path[::-1]

    def spanning_tree(self):
        tree = Graph()
        start_node = self.nodes["a"]
        queue = []
        tree.add_node(start_node.label, start_node.value)
        for edge in start_node.edges:
            heapq.heappush(queue, [edge.weight, edge])

        while queue:
            min_edge: Edge = heapq.heappop(queue)[1]
            next_node = min_edge.to_node

            if tree.nodes.__contains__(min_edge.to_node.label):
                continue

            tree.add_node(next_node.label, next_node.value)
            tree.connection(min_edge.from_node.label, next_node.label, min_edge.weight)

            for edge in next_node.edges:
                if tree.nodes.__contains__(edge.to_node.label):
                    continue
                heapq.heappush(queue, [edge.weight, edge])

        return tree







