# node.py
class node:
    def __init__(self, ID, net, x, y, r):
        self.id = ID
        self.env = net
        self.neighbors = []
        self.x = x
        self.y = y
        self.r = r
        self.on = True  # Used for visualization status if needed