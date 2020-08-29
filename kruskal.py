from operator import itemgetter

class Kruskal:

    def __init__(self):
        self.nodes = {}
        self.order = {}

    def prepare_structure(self, node): 
        self.nodes[node] = node # {2: 2, 5: 5}
        self.order[node] = 0 # {2: 0, 5:0}

    # {'a': 'd'}
    # {'d': 'd'}
    # {'f': 'd'}
    def find_node(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_node(self.nodes[node])
        return self.nodes[node]

    # {'a': 0}
    # {'d': 1}
    # {'f': 0 }
    def verify_union(self, origin, destination):
        init_node = self.find_node(origin)
        final_node = self.find_node(destination)
        if init_node != final_node:
            if self.order[init_node] > self.order[final_node]:
                self.nodes[final_node] = init_node
            else:
                self.nodes[init_node] = final_node
                if self.order[init_node] == self.order[final_node]:
                    self.order[final_node] += 1

    # nodes ['a', 'b', 'c'... , 'z']
    # array [ 0 ,  1 , 2]
    # edges ['a', 'g', 2]
    def apply_kruskal(self, nodes, edges):
        met = [] # Árbol de Expansion Mínima
        # met => [['a', 'd', 5], ['d', 'f', 6]]
        for node in nodes:
            self.prepare_structure(node)
        # Ordenamos las aristas de acuerdo al peso de menor a mayor
        edges.sort(key = itemgetter(2))
        # Recorremos las aristas para determinar el camino más eficiente a todos los nodos
        for edge in edges:
            # String origin = edge[0];
            # String destination = edge[1];
            # int weight = edge[2];
            origin, destination, weight = edge
            #                   a                            g
            if self.find_node(origin) != self.find_node(destination):
                self.verify_union(origin, destination)
                met.append(edge)
        return met