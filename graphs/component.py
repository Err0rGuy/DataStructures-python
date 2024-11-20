class Node:
    def __init__(self, label: str, value: int):
        self.label = label
        self.value = value
        self.edges: list[Edge] = []

    def __str__(self):
        return f'{self.label} : {self.value}'

    def remove_edge(self, target):
        for edge in self.edges:
            if edge.second_node.label == target.label:
                self.edges.remove(edge)

    def add_edge(self, target, weight):
        for edge in self.edges:
            if edge.second_node.label == target.label:
                raise Exception("This node is connected before!")
        self.edges.append(Edge(self, target, weight))


class Edge:
    def __init__(self, first_node: Node, second_node: Node, weight: int):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def __str__(self):
        return f'[{self.first_node} <--> {self.second_node} weight : {self.weight}]'

    def __lt__(self, other):
        return self.weight < other.weight
