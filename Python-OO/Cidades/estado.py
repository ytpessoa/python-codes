

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
    
    def adicionaCidade(self, cidade):
        self.cidades.append(cidade)
    
    def populacaoEstado(self): 
        self.totalPop = 0
        for cidade in self.cidades:
            self.totalPop += cidade.populacao        

        print(f"Total Populacao no Estado {self.nome} eh {self.totalPop}")