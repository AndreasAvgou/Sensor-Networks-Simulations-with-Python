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
        # Create nodes
        for i in range(self.pop):
            self.nodes.append(node(i, self, random.random() * self.xmax, random.random() * self.ymax, self.r))
        
        # Determine neighbors (O(N^2) complexity)
        for i in self.nodes:
            self.find_neighbors(i)

    def find_neighbors(self, node):
        for i in self.nodes:
            # Calculate Euclidean distance
            dist = self.distance(node, i)
            # If within radius r, and not self, add to neighbors
            if dist <= self.r and node.id != i.id:
                # Ensure we don't add duplicates if logic runs twice
                if i not in node.neighbors:
                    node.neighbors.append(i)
                if node not in i.neighbors:
                    i.neighbors.append(node)

    def distance(self, i, j):
        return math.sqrt((i.x - j.x)**2 + (i.y - j.y)**2)

    def metric(self):
        max_link = 0
        min_link = 10**6
        distr = distribution()
        edges = 0
        for i in range(self.pop):
            ei = len(self.nodes[i].neighbors)
            distr.add(ei)
            if ei > max_link:
                max_link = ei
            if ei < min_link:
                min_link = ei
            edges += ei
        edges /= 2
        # Optional: return stats instead of just printing
        return {
            "total_links": edges,
            "avg_links": edges * 2 / self.pop,
            "max_links": max_link,
            "min_links": min_link,
            "connected": self.is_connected()
        }

    def is_connected(self):
        # BFS / Flood Fill to check connectivity
        informed = set()
        start = 0 # Always start from node 0 for consistency
        to_inform = {self.nodes[start].id}
        
        while len(to_inform) > 0 and len(informed) < self.pop:
            to_inform_next = set()
            for i in to_inform:
                if i not in informed:
                    informed.add(self.nodes[i].id)
                    for j in self.nodes[i].neighbors:
                        if j.id not in informed:
                            to_inform_next.add(j.id)
            to_inform = to_inform_next
            
        return len(informed) == self.pop