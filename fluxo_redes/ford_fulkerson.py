from collections import deque
from aresta import Aresta

class FordFulkerson:
    def __init__(self, G, s: int, t: int):
        self.valor_fluxo: float = 0.0
        self.marcado: list[bool] = [False] * G.num_vertices()
        self.aresta_para: list[Aresta] = [None] * G.num_vertices()

        while self.caminho_aumentante(G, s, t):
            bottle = float('inf')
            v = t
            while v != s:
                bottle = min(bottle, self.aresta_para[v].capacidade_residual_para(v))
                v = self.aresta_para[v].outro(v)

            v = t
            while v != s:
                self.aresta_para[v].adicionar_fluxo_residual_para(v, bottle)
                v = self.aresta_para[v].outro(v)

            self.valor_fluxo += bottle

    def caminho_aumentante(self, G, s: int, t: int) -> bool:
        self.aresta_para = [None] * G.num_vertices()
        self.marcado = [False] * G.num_vertices()
        
        fila = deque([s])
        self.marcado[s] = True
        
        while fila:
            v = fila.popleft()
            for e in G.adjacentes(v):
                w = e.outro(v)
                if not self.marcado[w] and e.capacidade_residual_para(w) > 0:
                    self.aresta_para[w] = e
                    self.marcado[w] = True
                    fila.append(w)
                    
        return self.marcado[t]

    def valor(self) -> float:
        return self.valor_fluxo

    def em_corte(self, v: int) -> bool:
        return self.marcado[v]
