class Sobremesa:
    def __init__(self, nome, dataFabric):
        self.nome= nome
        self.dataFabric= dataFabric
    def get_nome(self):
        return self.nome
    def get_dataFabric(self):
        return self.dataFabric

    def set_nome(self, novoNome):
        self.nome= novoNome
    def set_dataFabric(self, novoData):
        self.dataFabric= novoData

    #Metodo criativo para usar em todos
    def aumentarAno(self):
        self.dataFabric= self.dataFabric+1

class Bolo (Sobremesa):
    def __init__(self, nome, dataFabric, qntFatias, qntRecheio=2):
        super().__init__(nome, dataFabric)
        self.qntFatias= qntFatias
        self.qntRecheio= qntRecheio

    def get_qntFatias(self):
        return self.qntFatias
    def get_qntRecheio(self):
        return self.qntRecheio

    def set_qntFatias(self, novoQntFatias):
        self.qntFatias= novoQntFatias
    def set_qntRecheio(self, novoQntRecheio):
        self.qntRecheio= novoQntRecheio

class Cookie (Sobremesa):
    def __init__(self, nome, dataFabric, saborChocolate, qntFeito=10):
        super().__init__(nome, dataFabric)
        self.saborChocolate = saborChocolate
        self.qntFeito = qntFeito

    def get_saborChocolate(self):
        return self.saborChocolate
    def get_qntFeito(self):
        return self.qntFeito

    def set_saborChocolate(self, novoSaborChocolate):
        self.saborChocolate = novoSaborChocolate
    def set_qntFeito(self, novoQntFeito):
        self.qntFeito = novoQntFeito