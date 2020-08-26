class Kruskal:

    def __init__(self):
        self.nodes = {}
        self.order = {}

    def prepare_structure(self, node): 
        self.nodes[node] = node # {2: 2, 5: 5}
        self.order[node] = 0 # {2: 0, 5:0}

    def verify_union(self, origin, destination):
        pass    