import heapq
import sys
import random
from graph.component import Node, Edge


class Graph:
    def __init__(self):
        self.nodes: dict[str: Node] = {}
        self.count = 0

    # checking node exists
    def node_exists(self, label):
        return label in self.nodes.keys()

    # node insertion
    def add_node(self, label: str, value: int):
        if self.node_exists(label):
            raise Exception("This label is reserved before!")
        else:
            self.nodes[label] = Node(label, value)
            self.count += 1

    # node deletion
    def remove_node(self, label: str):
        if not self.node_exists(label):
            raise Exception(f'{label} is not exists!')
        else:
            self.disconnect_all(label)
            self.nodes.pop(label)
            self.count -= 1

    # make connection between two nodes
    def connect(self, first_label, second_label, weight: int):
        if not self.node_exists(first_label):
            raise Exception(f'{first_label} is not exists!')
        if not self.node_exists(second_label):
            raise Exception(f'{second_label} is not exists!')
        first_node: Node = self.nodes[first_label]
        second_node: Node = self.nodes[second_label]
        first_node.add_edge(second_node, weight)
        second_node.add_edge(first_node, weight)

    # make two nodes disconnected
    def disconnect(self, first_label, second_label):
        if not self.node_exists(first_label):
            raise Exception(f'{first_label} is not exists!')
        if not self.node_exists(second_label):
            raise Exception(f'{second_label} is not exists!')
        first_node = self.nodes[first_label]
        second_node = self.nodes[second_label]
        first_node.remove_edge(second_node)
        second_node.remove_edge(first_node)

    # disconnect all nodes from this node
    def disconnect_all(self, label: str):
        self.nodes[label].edges.clear()
        for node in self.nodes.values():
            for edge in node.edges:
                if edge.second_node.label == label:
                    node.edges.remove(edge)

    # finding connected nodes to this node
    def find_all_neighbors(self, label):
        node = self.nodes[label]
        neighbors = []
        for edge in node.edges:
            neighbors.append(edge.second_node)
        return neighbors

    # used for checking nodes continuity
    def __depth_iteration(self, node, visited):
        visited.add(node)
        for neighbor in self.find_all_neighbors(node.label):
            if neighbor not in visited:
                self.__depth_iteration(self.nodes.get(neighbor.label), visited)

    # is connected graph? --> no separation between any node and the other nodes
    def is_connected_graph(self) -> bool:
        start_node = next(iter(self.nodes.values()))
        visited = set()
        self.__depth_iteration(start_node, visited)
        return len(visited) == len(self.nodes)

    # iteration and printing all nodes
    def iteration(self):
        for node in self.nodes.values():
            print(node.__str__())

    # printing all connections
    def print_connections(self):
        visited = set()
        for node in self.nodes.values():
            visited.add(node.label)
            for edge in node.edges:
                if not visited.__contains__(edge.second_node.label):
                    print(edge.__str__())

    # checking that a node is connected to another node
    def is_connected(self, first_label, second_label) -> bool:
        first_node = self.nodes.get(first_label)
        for edge in first_node.edges:
            if edge.second_node.label == second_label:
                return True
        return False

    # is a complete graph? --> {every node has n-1 edges} n = number of nodes
    def is_complete_graph(self) -> bool:
        number_of_nodes = len(self.nodes)
        for node in self.nodes.values():
            if len(node.edges) != number_of_nodes - 1:
                return False
        return True

    def has_eulerian_path(self) -> bool:
        number_of_odd_nodes = 0
        for node in self.nodes.values():
            if len(node.edges) % 2 == 1:
                number_of_odd_nodes += 1
        return number_of_odd_nodes == 2

    def has_eulerian_cycle(self) -> bool:
        if not self.is_connected_graph():
            return False
        for node in self.nodes.values():
            if len(node.edges) % 2 != 0:
                return False
        return True

    def has_hamiltonian_path(self) -> bool:
        random_node = random.choice(list(self.nodes.keys()))
        return self.__has_hamiltonian_path(random_node, None)

    def __has_hamiltonian_path(self, current_node_label, visited=None) -> bool:
        if visited is None:
            visited = set()
        visited.add(current_node_label)
        if len(visited) == len(self.nodes):
            return True
        current_node = self.nodes[current_node_label]
        for edge in current_node.edges:
            next_node_label = edge.second_node.label
            if next_node_label not in visited:
                if self.__has_hamiltonian_path(next_node_label, visited):
                    return True
        visited.remove(current_node_label)
        return False

    def has_hamiltonian_cycle(self, current_node_label) -> bool:
        return self.__has_hamiltonian_cycle(current_node_label, None)

    def __has_hamiltonian_cycle(self, current_node_label, visited=None) -> bool:
        if visited is None:
            visited = set()
        visited.add(current_node_label)
        if len(visited) == len(self.nodes):
            if self.is_connected(current_node_label, list(visited)[0]):
                return True
        current_node = self.nodes[current_node_label]
        for edge in current_node.edges:
            next_node_label = edge.second_node.label
            if next_node_label not in visited:
                if self.__has_hamiltonian_cycle(next_node_label, visited):
                    return True
        visited.remove(current_node_label)
        return False

    #Digesta --> finding shortest way between two nodes
    def shortest_way(self, first_label, second_label):
        if not self.node_exists(first_label):
            raise Exception(f'{first_label} is not exists!')
        if not self.node_exists(second_label):
            raise Exception(f'{second_label} is not exists!')
        first_node = self.nodes[first_label]
        second_node = self.nodes[second_label]
        visited = set()
        pre_nodes: dict[Node: Node] = {}
        distances: dict[Node: int] = {}
        priority_queue: list[tuple] = []
        for node in self.nodes.values():
            distances[node] = sys.maxsize
        distances[first_node] = 0
        heapq.heappush(priority_queue, (0, first_node))

        while priority_queue:
            current_node: Node = heapq.heappop(priority_queue)[1]
            if current_node not in visited:
                visited.add(current_node)
            for edge in current_node.edges:
                if not visited.__contains__(edge.second_node):
                    distance = distances[current_node] + edge.weight
                    if distance < distances[edge.second_node]:
                        distances[edge.second_node] = distance
                        heapq.heappush(priority_queue, (distance, edge.second_node))
                        pre_nodes[edge.second_node.label] = current_node.label

        path = [second_node.label]
        previous = pre_nodes.get(second_node.label)
        while not previous is None:
            path.append(" --> ")
            path.append(previous)
            previous = pre_nodes.get(previous)
        return path[::-1]

    # spanning tree --> deleting unnecessary edges but the nodes are still have way to each other
    def spanning_tree(self, start_node):
        if not self.node_exists(start_node):
            raise Exception(f'{start_node} does not exists!')
        first_node = self.nodes[start_node]
        tree = Graph()
        priority_queue: list[tuple[int, Edge]] = []
        for edge in first_node.edges:
            heapq.heappush(priority_queue, (edge.weight, edge))
        tree.add_node(first_node.label, first_node.value)
        while priority_queue:
            min_edge: Edge = heapq.heappop(priority_queue)[1]
            next_node = min_edge.second_node
            if not tree.node_exists(next_node.label):
                tree.add_node(next_node.label, next_node.value)
                tree.connect(min_edge.first_node.label, next_node.label, min_edge.weight)

            for edge in next_node.edges:
                if not tree.node_exists(edge.second_node.label):
                    heapq.heappush(priority_queue, (edge.weight, edge))
        return tree
