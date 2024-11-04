from grafo_rede_fluxo import GrafoRedeFluxo, Aresta
from ford_fulkerson import FordFulkerson

g = GrafoRedeFluxo(6)
g.add_aresta(Aresta(0, 1, 16))
g.add_aresta(Aresta(0, 2, 13))
g.add_aresta(Aresta(2, 1, 4))
g.add_aresta(Aresta(1, 3, 12))
g.add_aresta(Aresta(3, 2, 9))
g.add_aresta(Aresta(2, 4, 14))
g.add_aresta(Aresta(4, 3, 7))
g.add_aresta(Aresta(3, 5, 20))
g.add_aresta(Aresta(4, 5, 4))

ff = FordFulkerson(g, 0, 5)
print("Valor máximo do fluxo:", ff.valor())
print("Em corte:", [ff.em_corte(v) for v in range(g.V)])
