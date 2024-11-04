from aresta import Aresta

class GrafoRedeFluxo:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_aresta(self, e: Aresta):
        self.adj[e.de()].append(e)

    def adjacentes(self, v):
        return self.adj[v]

    def num_vertices(self):
        return self.V
