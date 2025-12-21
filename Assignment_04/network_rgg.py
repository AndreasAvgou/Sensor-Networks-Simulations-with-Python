# network_rgg.py
import random
import math
from node import node
from distribution import distribution

class network_rgg:
    def __init__(self, population, r):
        self.pop = population
        self.r = r
        self.nodes = []
        self.xmax = 1
        self.ymax = 1
        self.construct()

    def construct(self):
        self.nodes = []
        # Create nodes
        for i in range(self.pop):
            self.nodes.append(node(i, self, random.random() * self.xmax, random.random() * self.ymax, self.r))
        
        # Find neighbors (O(N^2) complexity)
        for i in self.nodes:
            self.find_neighbors(i)

    def find_neighbors(self, node):
        for i in self.nodes:
            # Distance check
            dist = self.distance(node, i)
            # If within radius, different node, and not already connected
            if dist <= self.r and node.id != i.id:
                if i not in node.neighbors:
                    node.neighbors.append(i)
                if node not in i.neighbors:
                    i.neighbors.append(node)

    def distance(self, i, j):
        return math.sqrt((i.x - j.x)**2 + (i.y - j.y)**2)

    def is_connected(self):
        """Checks if the graph is fully connected using BFS."""
        if self.pop == 0: return False
        informed = set()
        start = 0 
        to_inform = {self.nodes[start].id}
        
        while len(to_inform) > 0 and len(informed) < self.pop:
            to_inform_next = set()
            for i in to_inform:
                if i not in informed:
                    informed.add(i)
                    current_node = self.nodes[i]
                    for neighbor in current_node.neighbors:
                        if neighbor.id not in informed:
                            to_inform_next.add(neighbor.id)
            to_inform = to_inform_next
        return len(informed) == self.pop