# random_walker.py
import random

class random_walker:
    def __init__(self, net, start_node):
        self.net = net
        self.path = [start_node.id]
        self.visited = {start_node.id} # Set of unique IDs visited

    def next_step(self):
        # Get the current node object based on the last ID in path
        current_id = self.path[-1]
        current_node = self.net.nodes[current_id]
        
        if len(current_node.neighbors) > 0:
            # Pick a random neighbor
            next_node = random.choice(current_node.neighbors)
            self.path.append(next_node.id)
            self.visited.add(next_node.id)
        else:
            # If isolated node, stay put (should not happen in connected RGG with r=0.08)
            self.path.append(current_id)

    def get_coverage(self):
        return len(self.visited) / self.net.pop