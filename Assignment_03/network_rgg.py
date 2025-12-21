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
            if node.id != i.id:
                dist = self.distance(node, i)
                if dist <= self.r:
                    # Avoid duplicates in undirected graph logic
                    if i not in node.neighbors:
                        node.neighbors.append(i)
                    if node not in i.neighbors:
                        i.neighbors.append(node)

    def distance(self, i, j):
        return math.sqrt((i.x - j.x)**2 + (i.y - j.y)**2)

    def get_degree_stats(self):
        """
        Returns a tuple: (average_degree, max_degree, min_degree)
        """
        max_deg = 0
        min_deg = 10**6
        total_edges = 0
        
        for i in range(self.pop):
            deg = len(self.nodes[i].neighbors)
            
            if deg > max_deg:
                max_deg = deg
            if deg < min_deg:
                min_deg = deg
            
            total_edges += deg
            
        # Total edges count counts each link twice (once for each node), 
        # but here we sum degrees directly, so sum(degrees) / N = Avg Degree.
        avg_deg = total_edges / self.pop
        
        return avg_deg, max_deg, min_deg