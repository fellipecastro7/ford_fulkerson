class Aresta:
    def __init__(self, v, w, capacidade):
        self.v = v
        self.w = w
        self.capacidade = capacidade
        self.fluxo = 0.0

    def de(self):
        return self.v

    def para(self):
        return self.w

    def capacidade(self):
        return self.capacidade

    def fluxo(self):
        return self.fluxo

    def outro(self, vertice):
        if vertice == self.v:
            return self.w
        elif vertice == self.w:
            return self.v
        return None

    def capacidade_residual_para(self, vertice):
        if vertice == self.v:
            return self.fluxo  # Fluxo para v
        elif vertice == self.w:
            return self.capacidade - self.fluxo  # Capacidade restante
        return -1

    def adicionar_fluxo_residual_para(self, vertice, delta):
        if vertice == self.v:
            self.fluxo -= delta
        elif vertice == self.w:
            self.fluxo += delta
